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

Sphinx theme for Airflow
========================

Sphinx theme for Apache Airflow website.

# Getting started

In order to start working with the theme, please follow the instructions below.
1.  Make sure that your `python` shell command executes Python3 interpreter. If necessary, use a virtual environment:

    `mkvirtualenv -p python3 <name_of_environment>`

2.  To make Javascript and CSS code available for the theme, run the following command in the root directory:

    `./site.sh build-site && ./site.sh prepare-theme`

3.  To install the required Python packages, in `<ROOT DIRECTORY>/sphinx_airflow_theme` run:

    `pip install -e .`

4.  To launch the demo documentation page, in `<ROOT DIRECTORY>/sphinx_airflow_theme/demo` run:
    `./docs.sh build && ./docs.sh preview`

# Theme's source files

 - `<ROOT DIRECTORY>/sphinx_airflow_theme/sphinx_airflow_theme` - HTML files
 - `<ROOT DIRECTORY>/landing-pages/site/assets/scss` - SCSS files
 - `<ROOT DIRECTORY>/landing-pages/src/js` - Javascript files. If you create a new JS file, **don't forget to include it
  in** `<ROOT DIRECTORY>/landing-pages/src/docs-index.js
