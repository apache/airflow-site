#!/usr/bin/env python
import sys

import requests

resp = requests.get("https://live-docs-airflow-apache-org.s3.us-east-2.amazonaws.com/manifest/packages-metadata.json")
if resp.status_code != 200:
    raise RuntimeError(f"Failed to fetch metadata: {resp.status_code} - {resp.text}")

sys.stdout.write(resp.text)
