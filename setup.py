# Copyright 2020 The TensorFlow Recommenders Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""GCP UTILS"""

import pathlib
import setuptools

VERSION = "0.0.1"

REQUIRED_PACKAGES = [
    "pyftpdlib", "google-cloud"
]

long_description = (pathlib.Path(__file__).parent
                    .joinpath("README.md")
                    .read_text())

setuptools.setup(
    name="gcputils",
    version=VERSION,
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aburdenko",
    author="Alex Burdenko",
    author_email="alex.burdenko@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED_PACKAGES,
    extras_require={
    },
    # PyPI package information.
    classifiers=[],
    license="Apache 2.0",
    keywords=""
)
