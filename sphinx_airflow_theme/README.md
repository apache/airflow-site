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

Sphinx theme for Apache Airflow documentation.

# Install from sources

In order to start working with the theme, please follow the instructions below.

1.  Make sure your `python` shell command executes Python3 interpreter. If necessary, use a virtual environment:
    ```
    mkvirtualenv -p python3 <name_of_environment>
    ```

2.  To make Javascript and CSS code available for the theme, run the following command in the root directory:
    ```shell script
    ./site.sh build-site && ./site.sh prepare-theme
    ```

3.  To install the required Python packages, in `<ROOT DIRECTORY>/sphinx_airflow_theme` run:
    ```shell script
    pip install -e .
    ```

4.  To launch the demo documentation page, in `<ROOT DIRECTORY>/sphinx_airflow_theme/demo` run:
    ```shell script
    ./docs.sh build && ./docs.sh preview
    ```

# Install developer version

To install the latest development version of a theme, run:
```shell script
THEME_VERSION="$(curl -s https://api.github.com/repos/apache/airflow-site/releases/latest | grep '"tag_name":' | cut -d '"' -f 4)"
pip install "https://github.com/apache/airflow-site/releases/download/${THEME_VERSION}/sphinx_airflow_theme-${THEME_VERSION}-py3-none-any.whl"
```
Python packages for your PRs is available as downloadable artifact in GitHub Actions after
the CI builds your PR.

# Configuration

A theme that supports the following configuration options under the `html_theme_options` dict in your projects `conf.py`:

## `navbar_links`

The list of links that should be available in the navigation bar at the top of the pages. The order of items will not be changed.

**Example values:**
```python
html_theme_options = {
    'navbar_links': [
        {'href': '/docs/', 'text': 'Documentation'}
    ]
}
```

(This is the default)

## `hide_website_buttons`

If ``True``, all links on the same domain but not pointing to this theme's page (e.g. `/community/`) will be hidden.

**Example values:**
```python
html_theme_options = {
  'hide_website_buttons': False,
}
```

## `sidebar_collapse`
## `sidebar_includehidden`

Controls the ToC display in the sidebar. See https://www.sphinx-doc.org/en/master/templating.html#toctree for more info

# Theme's source files

 - `<ROOT DIRECTORY>/sphinx_airflow_theme/sphinx_airflow_theme` - HTML files
 - `<ROOT DIRECTORY>/landing-pages/site/assets/scss` - SCSS files
 - `<ROOT DIRECTORY>/landing-pages/src/js` - Javascript files. If you create a new JS file, **don't forget to include it
  in** `<ROOT DIRECTORY>/landing-pages/src/docs-index.js
