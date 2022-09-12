from gcputils.Interface import Interface
from gcputils.cloud_storage import download_str_from_bucket
from gcputils.credentials import get_credentials



def abstractmethod(func):
    func.__isabstract__ = True
    return func

class FileConverter( object, metaclass=Interface):                   
    def __init__(self, project_id: str, input_gcs_uri: str, first_gcs_uri : str, updated_timestamp_str : str):
        self._project_id = project_id
        self._input_gcs_uri = input_gcs_uri        
        self._first_gcs_uri = first_gcs_uri
        self._updated_timestamp_str = updated_timestamp_str

        self._output_path = None
        GOOGLE_APPLICATION_CREDENTIALS = '/content/service_account.json'        
        self._creds = get_credentials( service_account_file=GOOGLE_APPLICATION_CREDENTIALS)
        
        self._clean_file_path, self._file_name, self._file_prefix , self._file_ext, self._sub_folder = self._get_clean_path( input_gcs_uri )
                    
        import re
        matches = re.match(r"gs://(.*?)/(.*)", input_gcs_uri)
    
        if matches:    
            bucket_name, path_prefix = matches.groups()
            self._bucket_name=bucket_name
            self._content = download_str_from_bucket( bucket_name=bucket_name, file_path=path_prefix )

    def _sanitize_input_path(self, in_path: str):
        in_path = in_path.replace( ', ', '_')
        in_path = in_path.replace( ' ', '_')
        in_path = in_path.replace( '\#', 'number')
        in_path = in_path.replace( '#', 'number')
        in_path = in_path.replace( '.', '_')
        in_path = in_path.replace( '/', '_')

        return in_path
    

    def _get_clean_path(self, input_gcs_source: str) -> tuple:    
        str_array = input_gcs_source.split('/')
        folder = str_array[-2] 
        raw_file_name = str_array[-1] 
        import os
        file_prefix=os.path.splitext(raw_file_name )[0] 
        file_ext = os.path.splitext(raw_file_name )[1] 

        clean_file_path = self._sanitize_input_path(raw_file_name)
        print(f"clean_file_path: {clean_file_path}")
        return (clean_file_path, raw_file_name, file_prefix, file_ext, folder)

    def to_jsonl( self,  entity_list : list):
        import json
        from io import StringIO
        
        res = [json.dumps(record) for record in entity_list]    
        buf = StringIO()
        for i in res:
            buf.write(i+'\n')
        
        sbuf = buf.getvalue().replace('"-','\"-')
        sbuf = buf.getvalue().replace("'-","-")
        sbuf = buf.getvalue().replace("'","\"")
        sbuf = buf.getvalue().replace("#","\#")
        
        return sbuf

    @abstractmethod            
    def process( self, **kwargs ):    
        pass
           
    def __repr__(self):
        return str(self.__dict__)