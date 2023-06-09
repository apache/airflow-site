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
import enum
import logging
import os
import sys
from urllib.request import urlopen
import semver

airflow_redirects_link = "https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/redirects.txt"
helm_redirects_link = "https://raw.githubusercontent.com/apache/airflow/main/docs/helm-chart/redirects.txt"
providers_redirect_link = "populate-this"

docs_archive_path = "../docs-archive"
airflow_docs_path = docs_archive_path + "/apache-airflow"
helm_docs_path = docs_archive_path + "/helm-chart"
providers_docs_path = docs_archive_path + "/apache-airflow-providers"

# version where changes were introduced in docs structure
new_airflow_docs_version = "2.5.1"
new_helm_docs_version = "1.6.0"
# change this correctly
new_providers_docs_version = "0.0.0"


# types of generations supported
class GenerationType(enum.Enum):
    airflow = 1
    helm = 2
    providers = 3


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


def version_is_less_than(a, baseline):
    return semver.compare(a, baseline) == -1


def get_redirect_content(url: str):
    return f'<html><head><meta http-equiv="refresh" content="0; url={url}"/></head></html>'


def create_back_reference_html(back_ref_url, path):
    content = get_redirect_content(back_ref_url)

    # Creating an HTML file
    with open(path, "w") as f:
        f.write(content)


def generate_back_references(link, base_path, change_version):
    download_file(link)
    old_to_new = construct_mapping()

    versions = [f.path.split("/")[-1] for f in os.scandir(base_path) if f.is_dir()]
    versions = [v for v in versions if version_is_less_than(v, change_version)]

    for version in versions:
        r = base_path + "/" + version

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


# total arguments
n = len(sys.argv)
if n != 2:
    logging.Logger.error("missing required arguments, syntax: python add-back-references.py [airflow | providers | "
                         "helm]")

gen_type = GenerationType[sys.argv[1]]
if gen_type == GenerationType.airflow:
    generate_back_references(airflow_redirects_link, airflow_docs_path, new_airflow_docs_version)
elif gen_type == GenerationType.helm:
    generate_back_references(helm_redirects_link, helm_docs_path, new_helm_docs_version)
elif gen_type == GenerationType.providers:
    # solve this properly for different providers
    generate_back_references(providers_redirect_link, providers_docs_path, new_providers_docs_version)
else:
    logging.Logger.error("invalid type of doc generation required. Pass one of [airflow | providers | "
                         "helm]")
