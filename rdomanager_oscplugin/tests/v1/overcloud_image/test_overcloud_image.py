#   Copyright 2015 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from rdomanager_oscplugin.tests.v1.test_plugin import TestPluginV1

# Load the plugin init module for the plugin list and show commands
from rdomanager_oscplugin.v1 import overcloud_image


class FakePluginV1Client(object):
    def __init__(self, **kwargs):
        self.auth_token = kwargs['token']
        self.management_url = kwargs['endpoint']


class TestOvercloudImageBuild(TestPluginV1):

    def setUp(self):
        super(TestOvercloudImageBuild, self).setUp()

        # Get the command object to test
        self.cmd = overcloud_image.BuildPlugin(self.app, None)


class TestOvercloudImageCreate(TestPluginV1):
    def setUp(self):
        super(TestOvercloudImageCreate, self).setUp()

        # Get the command object to test
        self.cmd = overcloud_image.CreatePlugin(self.app, None)
