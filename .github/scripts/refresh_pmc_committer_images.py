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
#   "rich>=13.3.4",
#   "requests>=2.32.2",
# ]
# ///

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
import json
from rich.console import Console

console = Console(width=400, color_system="standard")

AIRFLOW_SOURCES_ROOT = Path(__file__).parents[2]
PROFILES_DIR = AIRFLOW_SOURCES_ROOT / "landing-pages/site/static/external/profiles"

MAX_WORKERS = 20


def download_image(data: dict) -> str | None:
    github_url = data.get("github")
    username = github_url.split("/")[-1]
    image_url = github_url + ".png"
    name = data.get("name")
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            (PROFILES_DIR / f"{username}.png").write_bytes(response.content)
            return None
        else:
            return f"Failed to download image for {name} (HTTP {response.status_code})"
    except Exception as e:
        return f"Failed to download image for {name}: {e}"


def refresh_committer_pmc_images(file_path: Path):
    with open(file_path) as f:
        pmc_committer_data = json.load(f)
    console.print(f"Downloading [cyan]{len(pmc_committer_data)}[/] images from [magenta]{file_path.name}[/] ({MAX_WORKERS} parallel workers)")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(download_image, data): data for data in pmc_committer_data}
        for future in as_completed(futures):
            error = future.result()
            if error:
                console.print(f"[red]{error}[/]")
    console.print(f"[green]Done with {file_path.name}[/]")


if __name__ == "__main__":
    pmc_committer_files = os.environ.get("PMC_COMMITTERS_FILES",
                                         "landing-pages/site/data/committers.json,landing-pages/site/data/pmc.json")
    if pmc_committer_files:
        for file_path in pmc_committer_files.split(","):
            refresh_committer_pmc_images(AIRFLOW_SOURCES_ROOT / file_path)
