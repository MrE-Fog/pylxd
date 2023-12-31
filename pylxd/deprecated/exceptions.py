# Copyright (c) 2015 Canonical Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class PyLXDException(Exception):
    pass


class ContainerUnDefined(PyLXDException):
    pass


class UntrustedHost(PyLXDException):
    pass


class ContainerProfileCreateFail(PyLXDException):
    pass


class ContainerProfileDeleteFail(PyLXDException):
    pass


class ImageInvalidSize(PyLXDException):
    pass


class APIError(PyLXDException):
    def __init__(self, error, status_code):
        msg = f"Error {status_code} - {error}."
        super().__init__(msg)
        self.status_code = status_code
        self.error = error
