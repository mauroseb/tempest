# Copyright 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tempest.cmd import cleanup
from tempest.tests import base


class TestTempestCleanup(base.TestCase):

    def test_load_json(self):
        # instatiate "empty" TempestCleanup
        c = cleanup.TempestCleanup(None, None, 'test')
        test_saved_json = 'tempest/tests/cmd/test_saved_state_json.json'
        # test if the file is loaded without any issues/exceptions
        c._load_json(test_saved_json)
