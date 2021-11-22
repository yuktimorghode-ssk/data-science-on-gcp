# Copyright 2021 Google Inc. All Rights Reserved.
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

import os

CHANGES = [
    # both
    ("ch9", "ch10"),

    # train_on_vertexai.py
    ("ENDPOINT_NAME = 'flights'", "ENDPOINT_NAME = 'flights-ch10'"),

    # model.py
    ("arr_airport_lat,arr_airport_lon", "arr_airport_lat,arr_airport_lon,avg_dep_delay,avg_taxi_out")
]

for filename in ['train_on_vertexai.py', 'model.py']:
    in_filename = os.path.join('../09_vertexai', filename)
    with open(in_filename, "r") as ifp:
        with open(filename, "w") as ofp:
            for line in ifp.readlines():
                for change in CHANGES:
                    new_line = line.replace(change[0], change[1])
                    if new_line != line:
                        print('<<' + line + '>>' + new_line)
                        line = new_line
                ofp.write(line)
