#!/usr/bin/env python
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
# PEP 723 compliant inline script metadata
# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "requests>=2.32.2",
# ]
# ///

import sys

import requests
import os

bucket = os.environ.get("S3_DOCS_BUCKET", "live-docs-airflow-apache-org")
resp = requests.get(f"https://{bucket}.s3.us-east-2.amazonaws.com/manifest/packages-metadata.json")
if resp.status_code != 200:
    raise RuntimeError(f"Failed to fetch metadata: {resp.status_code} - {resp.text}")

sys.stdout.write(resp.text)
