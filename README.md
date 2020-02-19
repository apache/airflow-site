<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->

Apache Airflow website
======================

[![Build Status](https://travis-ci.org/apache/airflow-site.svg)](https://travis-ci.org/apache/airflow-site)

This is a repository of [Apache Airflow website](https://airflow.apache.org).
The repository of Apache Airflow can be found [here](https://github.com/apache/airflow/).

# General directory structure

- docs-archive - directory containing archived documentation versions and shell script generating docs index,
- landing-pages - directory containing the source code of landing pages,
- license-templates - directory containing license templates,
- sphinx_airflow_theme - directory containing source code of sphinx theme for Apache Airflow documentation site.

For more detailed description of directory structure, please refer to [contributor's guide](CONTRIBUTE.md).

# Getting started

If you're a Macbook user, first install `coreutils`.

`brew install coreutils`

---

The Docsy theme required for the site to work properly is included as a git submodule.

This means that after you already cloned the repository, you need to update submodules

```bash
git submodule update --init --recursive
```
---

In order to build site, run script `<ROOT DIRECTORY>/site.sh build-site`.

In order to preview landing pages, run script `<ROOT DIRECTORY>/site.sh preview-landing-pages`.

In order to work with documentation theme, please refer to
[Sphinx Airflow theme's readme file](sphinx_airflow_theme/README.md).

For more detailed description of `site.sh` capabilities, please refer to [contributor's guide](CONTRIBUTE.md).

# [Contributor's guide](CONTRIBUTE.md)

If you'd like to contribute to the Apache Airflow website project, read our [contributor's guide](CONTRIBUTE.md)
where you can find detailed instructions on how to work with the website.
