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
from ockb import ockb
import os, sys, signal, time

class OckbMaster(Script):
    def install(self, env):
        import params
        env.set_params(params)
        self.install_packages(env)

    def configure(self, env):
        import params
        env.set_params(params)
        ockb()

    def start(self, env, upgrade_type=None):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("{ockb_bin}/ockb >> {ockb_log_dir}/ockb.log & echo $! > {ockb_pid_file} &")
        Execute(start_cmd)

    def stop(self, env, upgrade_type=None):
        import params
        env.set_params(params)
        if os.path.isfile(params.ockb_pid_file):
            pid = int(file(params.ockb_pid_file,'r').readlines()[0])
            os.kill(pid, signal.SIGKILL)
            File(params.ockb_pid_file, action = "delete")

    def status(self, env):
        import params
        env.set_params(params)
        check_process_status(params.ockb_pid_file)

if __name__ == "__main__":
    OckbMaster().execute()