#   Copyright 2012-2015 Rackspace
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import setuptools


extensions = [
    'rackspace-auth-neutronclientext',                  # RAX-KSKEY
    'python_neutronclient_ip_address_extension',        # ip-address-*
]


setuptools.setup(
    name='rackspace-neutronclient',
    version='1.1',
    author='Rackspace',
    author_email='neutron-requests@lists.rackspace.com',
    description='Metapackage to install rackspace-python-neutronclient and '
                'Rackspace extensions',
    license='Apache License, Version 2.0',
    url='https://github.com/rackerlabs/rackspace-neutronclient',
    install_requires=['rackspace-python-neutronclient'] + extensions,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
