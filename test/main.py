#!/usr/bin/python
# Copyright (c) 2013 Qubell Inc., http://qubell.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest
from qubell.api.private.platform import QubellPlatform, Context

parameters = {
    'organization': os.getenv('QUBELL_ORGANIZATION', None),
    'user': os.environ['QUBELL_USER'],
    'pass': os.environ['QUBELL_PASS'],
    'tenant': os.environ['QUBELL_TENANT'],
    'provider_name': os.getenv('PROVIDER_NAME', "test-provider"),
    'provider_type': os.getenv('PROVIDER_TYPE', None),
    'provider_identity': os.getenv('PROVIDER_IDENTITY', None),
    'provider_credential': os.getenv('PROVIDER_CREDENTIAL', None),
    'provider_region': os.getenv('PROVIDER_REGION', None)
}

context = Context(user=parameters['user'], password=parameters['pass'], api=parameters['tenant'])
platform = QubellPlatform(context=context)
assert platform.authenticate()

if __name__ == '__main__':
    unittest.main(argv=["qubell-test", "discover", "--pattern=test*.py"])