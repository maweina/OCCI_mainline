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
from resource_management import *
import sys
from copy import deepcopy


def ockb(role=None):
    import params
    directories = [params.ockb_home,
                   params.ockb_log_dir,
                   params.ockb_pid_dir,
                   params.ockb_server_conf_dir]

    Directory(directories,
              owner=params.ockb_user,
              group=params.ockb_user_group,
              mode=0755,
              cd_access='a'
              )

    File(format("{ockb_server_conf_dir}/config.js"),
         content=Template(format("config.js.j2")),
         owner=params.ockb_user,
         group=params.ockb_user_group,
         mode=0644
         )

    File(format("{ockb_bin}/server"),
         content=Template(format("server.j2")),
         owner=params.ockb_user,
         group=params.ockb_user_group,
         mode=0755
         )