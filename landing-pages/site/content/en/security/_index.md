---
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
title: "Security"
linkTitle: "Security"
description: "How to report a security vulnerability in Apache Airflow, and every CVE published for Apache Airflow, its providers and related packages."
menu:
  main:
    weight: 3
---

# Security

## Reporting a vulnerability

Please report security vulnerabilities **privately** by email to
[security@airflow.apache.org](mailto:security@airflow.apache.org), not on GitHub issues, discussions,
pull requests, Slack or the public mailing lists. The Apache Airflow security team follows the
[Apache Software Foundation's vulnerability handling process](https://www.apache.org/security/):
we confirm receipt, assess the report, fix valid issues in a release, and then publish a CVE and an
announcement on the [users@airflow.apache.org](https://lists.apache.org/list.html?users@airflow.apache.org)
mailing list.

Before reporting, please read the
[Airflow Security Model](https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html).
It explains which users are trusted with which capabilities: behaviour that the model describes as
expected for a given role (for example, DAG authors running arbitrary code) is not a vulnerability.

## Published CVEs

The list below contains every CVE the Apache Software Foundation has published for Apache Airflow,
its providers and related packages, newest first. Each entry is built from the CVE record published
on [cve.org](https://www.cve.org/); the record on cve.org is authoritative. The severity shown is
the rating assigned by the Apache Airflow security team.
