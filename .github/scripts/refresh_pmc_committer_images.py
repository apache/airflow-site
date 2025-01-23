# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import requests
import json
def refresh_committer_pmc_images(file_path):

    with open(file_path) as f:
        pmc_committer_data = json.load(f)
    for data in pmc_committer_data:
        github_url = data.get("github")
        username = github_url.split("/")[-1]
        image_url = github_url+'.png'
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(f'landing-pages/site/static/external/profiles/{username}.png', 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download image for {data.get('name')}")


if __name__ == "__main__":
    pmc_committer_files = os.environ.get("PMC_COMMITTERS_FILES")
    if pmc_committer_files:
        file_paths = pmc_committer_files.split(",")
        for file_path in file_paths:
            refresh_committer_pmc_images(file_path)
