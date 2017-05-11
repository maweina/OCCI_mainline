#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
from resource_management.libraries.functions import format
from resource_management.libraries.script.script import Script

config = Script.get_config()

ockb_pid_dir = config['configurations']['ockb-env']['ockb_pid_dir']
ockb_pid_file = format("{ockb_pid_dir}/ockb.pid")

logstash_pid_dir = config['configurations']['logstash-env']['logstash_pid_dir']
logstash_pid_file = format("{logstash_pid_dir}/logstash.pid")
logstash_ha_pid_file = format("{logstash_pid_dir}/logstash_ha.pid")

elastic_pid_dir = config['configurations']['elastic-env']['elastic_pid_dir']
elastic_pid_file = format("{elastic_pid_dir}/elasticsearch.pid")

kibana_pid_dir = config['configurations']['kibana-env']['kibana_pid_dir']
kibana_pid_file = format("{kibana_pid_dir}/kibana.pid")