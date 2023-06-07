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
from urllib.request import urlopen
import semver

docs_link = "https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/redirects.txt"
docs_archive_path = "../docs-archive"
apache_airflow_path = docs_archive_path + "/apache-airflow"
stable_version_path = apache_airflow_path + "/stable.txt"
new_docs_version = "2.5.1"


def download_file(url):
    filedata = urlopen(url)
    datatowrite = filedata.read()

    with open('redirects.txt', 'wb') as f:
        f.write(datatowrite)


def construct_mapping():
    old_to_new_map = dict()
    with open('redirects.txt') as f:
        file_content = []
        lines = f.readlines()
        # Skip empty line

        for line in lines:
            if not line.strip():
                continue

            # Skip comments
            if line.startswith("#"):
                continue

            line = line.rstrip()
            file_content.append(line)

            old_path, new_path = line.split(" ")
            old_path = old_path.replace(".rst", ".html")
            new_path = new_path.replace(".rst", ".html")

            old_to_new_map[old_path] = new_path
    return old_to_new_map


def version_is_less_than(a):
    return semver.compare(a, new_docs_version) == -1


def get_redirect_content(url: str):
    return f'<html><head><meta http-equiv="refresh" content="0; url={url}"/></head></html>'


def create_back_reference_html(back_ref_url, path):
    content = get_redirect_content(back_ref_url)

    # Creating an HTML file
    with open(path, "w") as f:
        f.write(content)


download_file(docs_link)
old_to_new = construct_mapping()

versions = [f.path.split("/")[-1] for f in os.scandir(apache_airflow_path) if f.is_dir()]
versions = [v for v in versions if version_is_less_than(v)]

for version in versions:
    r = apache_airflow_path + "/" + version

    for p in old_to_new:
        old = p
        new = old_to_new[p]

        # only if old file exists, add the back reference
        if os.path.exists(r + "/" + p):
            d = old_to_new[p].split("/")
            file_name = old_to_new[p].split("/")[-1]
            dest_dir = r + "/" + "/".join(d[: len(d) - 1])

            # finds relative path of old file wrt new, handles case of different file names too
            relative_path = os.path.relpath(old, new)
            # remove one directory level because file path was used above
            relative_path = relative_path.replace("../", "", 1)

            os.makedirs(dest_dir, exist_ok=True)
            dest_file_path = dest_dir + "/" + file_name
            create_back_reference_html(relative_path, dest_file_path)
