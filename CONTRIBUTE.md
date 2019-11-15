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

## General directory structure

```bash
.
├── dist
├── docs-archive
├── landing-pages
│   ├── dist
│   ├── site
│   │   ├── assets
│   │   │   ├── icons
│   │   │   └── scss
│   │   ├── content
│   │   │   └── en
│   │   │       ├── blog
│   │   │       ├── community
│   │   │       ├── docs
│   │   │       ├── install
│   │   │       ├── meetups
│   │   │       ├── privacy-notice
│   │   │       ├── roadmap
│   │   │       └── use-cases
│   │   ├── data
│   │   ├── layouts
│   │   ├── static
│   │   │   ├── icons
│   │   │   └── integration-logos
│   │   └── themes
│   │       └── docsy
│   └── src
│       └── js
├── license-templates
└── sphinx_airflow_theme
    ├── demo
    └── sphinx_airflow_theme
```

## Working with the project

In order to run an environment for the project, make sure that you have Docker installed. Then, use the `site.sh`
script to work with the website in a Docker container.

`site.sh` provides the following commands.

    build-site              Prepare dist directory with landing pages and documentation
    preview-site            Starts the web server with preview of the website
    build-landing-pages     Builds a landing pages
    prepare-theme           Prepares and copies files needed for the proper functioning of the sphinx theme.
    shell                   Start shell
    build-image             Build a Docker image with a environment
    install-node-deps       Download all the Node dependencies
    check-site-links        Checks if the links are correct in the website
    lint-css                Lint CSS files
    lint-js                 Lint Javascript files
    cleanup                 Delete the virtual environment in Docker
    stop                    Stop the environment
    help                    Display usage

### How to add a new blogpost

In order to add a new blogpost, create a markdown file in `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/blog/<filename>.md`.
The filename will also serve as URL for your blogpost.

Then, **at the top of the file**, add frontmatter in following format:

    ---
    title: "<blogpost title>"
    linkTitle: "<blogpost link title>"
    author: "<author's name>"
    twitter: "<optional - author's Twitter ID>"
    github: "<optional - author's Github ID>"
    linkedin: "<optional - author's Linkedin ID>"
    description: "<short description>"
    tags: ["<tag1>", "<tag2>", ...]
    date: <date in YYYY-MM-DD format>
    ---

Below frontmatter, put your blogpost content.


### How to add a new case study

In order to add a new case study, create a markdown file in `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/use-cases/<filename>.md`.
The filename will also serve as URL for the case study.

Then, **at the top of the file**, add frontmatter in following format:

    ---
    title: "<case study title>"
    linkTitle: "<case study link title>"
    quote:
        text: "<quote text>"
        author: "<quote author's name>"
    logo: "<logo filename (with extension)>"
    ---

Below frontmatter, put your blogpost content in following format:

    #### What was the problem?
    <text>

    ##### How did Apache Airflow help to solve this problem?
    <text>

    #### What are the results?
    <text>

**Important** - put the logo file in `<ROOT DIRECTORY>/landing-pages/site/static/icons/` directory. Then, in the frontmatter,
refer to it just by filename.

Example:

    Path to logo file: <ROOT DIRECTORY>/landing-pages/site/static/icons/my-case-study.svg

    Case study in <ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/use-cases/my-case-study.md

    ---
    title: "<case study title>"
    linkTitle: "<case study link title>"
    quote:
        text: "<quote text>"
        author: "<quote author's name>"
    logo: "my-case-study.svg"
    ---

    #### What was the problem?
    <text>

    ##### How did Apache Airflow help to solve this problem?
    <text>

    #### What are the results?
    <text>

### How to add a new integration

In order to add a new integration, add an entry in `<ROOT DIRECTORY>/landing-pages/site/static/integrations.json` file,
following the format:
```json
{
  "name": "<integration name>",
  "url": "<url to docs with integration description>",
  "logo": "</integration-logos/<filename with extension>"
}
```

Integrations are displayed in random order, which might be different on each site reload. To search
for your integration, use the search functionality.

Providing an integration logo is **optional**. However, please take note that integrations with logo are be promoted
by being displayed before integrations without a logo.

### How to add a new meetup
In order to add an upcoming meetup, find your group in `<ROOT DIRECTORY>/landing-pages/site/static/meetups.json` file
and put the meetup's date in following format:

`MON, JAN 01, 6:00 PM`

If your meetup group isn't on the list, add it following the format of existing entries.

### How to release new documentation
To release a new documentation, follow these steps:

1.  In Apache Airflow's website root directory, run:

        <WEBSITE ROOT DIRECTORY>/site.sh prepare-theme
        cd <WEBSITE ROOT DIRECTORY>/sphinx_airflow_template
        pip install -e .

2.  In Apache Airflow's (not website!) root directory, run:

        pip install -e '.[doc]'
        cd docs/
        export GITHUB_VERSION="master"
        make html

3.  Copy generated files from `<APACHE AIRFLOW ROOT DIR>/docs/_build/html` to `<WEBSITE ROOT DIRECTORY>/docs-archive/<version>/`

4.  Make a commit with generated documentation only.

5.  To generate full website with documentation, run:

        <WEBSITE ROOT DIRECTORY>/site.sh build-site
