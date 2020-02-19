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

Contributor Guide
=================

```
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

# Working with the project

Work with the site and documentation requires that your computer be properly prepared. Most tasks can
be done by the site.sh script

### Prerequisite Tasks

The following applications must be installed to use the project:

* git
* docker

It is also worth adding SSH keys for the `github.com` server to trusted ones. It is necessary to clone repositories. You can do this using following command:
```bash
ssh-keyscan -t rsa -H github.com >> ~/.ssh/known_hosts
```

**Debian instalation**

To install git on Debian, run the following command:
```bash
sudo apt install git -y
```

To install docker, run the following command:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER
```

Git must have commit author information configured, run these commands
```bash
git config --global user.email '<your.email@example.com>'
git config --global user.name '<you name>'
```

### Static checks

The project uses many static checks using fantastic [pre-commit](https://pre-commit.com/). Every change is checked on CI and if it does not pass the tests it cannot be accepted. If you want to check locally then you should install Python3.6 or newer together with pip and run following command to install pre-commit:

```bash
pip install -r requirements.txt
```

To turn on pre-commit checks for commit operations in git, enter:
```bash
pre-commit install
```

To run all checks on your staged files, enter:
```bash
pre-commit run
```

To run all checks on all files, enter:
```bash
pre-commit run --all-files
```

Pre-commit check results are also attached to your PR through integration with Travis CI.

### Clone repository

To clone repository from github.com to local disk, run following command

```bash
git clone git@github.com:apache/airflow-site.git
git submodule update --init --recursive
```

### Use `site.sh` script

In order to run an environment for the project, make sure that you have Docker installed. Then, use the `site.sh`
script to work with the website in a Docker container.

`site.sh` provides the following commands.

    build-site            Prepare dist directory with landing pages and documentation
    preview-landing-pages Starts the web server with preview of the website
    build-landing-pages   Builds a landing pages
    prepare-theme         Prepares and copies files needed for the proper functioning of the sphinx theme.
    shell                 Start shell
    build-image           Build a Docker image with a environment
    install-node-deps     Download all the Node dependencies
    check-site-links      Checks if the links are correct in the website
    lint-css              Lint CSS files
    lint-js               Lint Javascript files
    cleanup               Delete the virtual environment in Docker
    stop                  Stop the environment
    help                  Display usage

### How to add a new blogpost

To add a new blogpost with pre-filled frontmatter, in `<ROOT DIRECTORY>/landing-pages/site` run:
```bash
hugo new blog/my-new-blogpost.md
```

That will create a markdown file `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/blog/my-new-blogpost.md`
with following content:
```
---
title: "My New Blogpost"
linkTitle: "My New Blogpost"
author: "Your Name"
twitter: "Your Twitter ID (optional, remove if not needed)"
github: "Your Github ID (optional, remove if not needed)"
linkedin: "Your LinkedIn ID (optional, remove if not needed)"
description: "Description"
tags: []
date: "2019-11-19"
draft: true
---
```
Below frontmatter, put your blogpost content.

When you finish your writing blogpost, remember to **remove `draft: true`** from frontmatter.

---

To add a new blogpost manually, create a markdown file in `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/blog/<filename>.md`.
The filename will also serve as URL for your blogpost.

Then, **at the top of the file**, add frontmatter in following format:
```
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
```
Below frontmatter, put your blogpost content.

### How to add a new case study

To add a new case study with pre-filled frontmatter, in `<ROOT DIRECTORY>/landing-pages/site` run:
```bash
hugo new use-cases/my-use-case.md
```

That will create a markdown file `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/use-cases/my-use-case.md`
with following content:
```
---
title: "My Use Case"
linkTitle: "My Use Case"
quote:
    text: "Quote text"
    author: "Quote's author"
logo: "logo-name-in-static-icons-directory.svg"
draft: true
---

##### What was the problem?
text

##### How did Apache Airflow help to solve this problem?
text

##### What are the results?
text
```
When you finish your writing blogpost, remember to **remove `draft: true`** from frontmatter.

---

To add a new case study manually, create a markdown file in `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/use-cases/<filename>.md`.
The filename will also serve as URL for the case study.

Then, **at the top of the file**, add frontmatter in following format:

```
---
title: "<case study title>"
linkTitle: "<case study link title>"
quote:
    text: "<quote text>"
    author: "<quote author's name>"
logo: "<logo filename (with extension)>"
---
```
Below frontmatter, put your blogpost content in following format:

```
#### What was the problem?
<text>

##### How did Apache Airflow help to solve this problem?
<text>

#### What are the results?
<text>

---
```

**Important** - put the logo file in `<ROOT DIRECTORY>/landing-pages/site/usecase-logos/icons/` directory. Then, in the frontmatter,
refer to it just by filename.

Example:

Path to logo file: <ROOT DIRECTORY>/landing-pages/site/static/usecase-logos/my-case-study.svg

Case study in <ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/use-cases/my-case-study.md

```
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
```

### How to add a new integration

In order to add a new integration, add an entry in `<ROOT DIRECTORY>/landing-pages/site/static/integrations.json` file,
following the format:
```json
{
  "name": "<integration name>",
  "url": "<url to docs with integration description>",
  "logo": "/integration-logos/<filename with extension>"
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

# How to release new documentation

Building documentation for the Apache Airlfow project also requires Python3.6 with pip and graphviz. You also need to have additional `apache/airflow` repository available.

### Prerequisite Tasks

You should install and set up all software from "Working with the project/Prerequisite tasks" section.

The following additional application must be installed to use the project:

* python3.6 or newer
* pip
* graphviz

**Debian instatation:**

To install graphviz, pip for Debian, run following commands:
```bash
sudo apt install graphviz python3-pip -y
```

You should also add `$HOME/.local/bin` to `$PATH`, run followin command:
```bash
export PATH=$HOME/.local/bin:$PATH;
```


### Clone repositories

It is necessary to configure 2 variables that point to directories with repositories and one that describe current Airflow version. The next steps will assume that these variables are available.
```bash
AIRFLOW_REPO=$HOME/airflow
AIRFLOW_SITE_REPO=$HOME/airflow-site
AIRFLOW_VERSION=1.10.9
```

```bash
git clone git@github.com:apache/airflow.git "${AIRFLOW_REPO}"
git clone git@github.com:apache/airflow-site.git "${AIRFLOW_SITE_REPO}"

cd "${AIRFLOW_SITE_REPO}" && git submodule update --init --recursive
```

### Instruction

To release a new documentation, follow these steps:

1.  To prepare and insstall Sphinx theme, run following commands:
    ```bash
    cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-site
    cd "${AIRFLOW_SITE_REPO}" && bash site.sh prepare-theme
    cd "${AIRFLOW_SITE_REPO}/sphinx_airflow_theme" && pip3 install -e .
    ```
2.  To build documentation, run following commands:
    ```bash
    cd "${AIRFLOW_REPO}" && git checkout "${AIRFLOW_VERSION}"
    cd "${AIRFLOW_REPO}" && pip3 install -e '.[doc]'
    cd "${AIRFLOW_REPO}/docs/" && bash build.sh
    ```

3.  Copy generated files from `${AIRFLOW_REPO}/docs/_build/html` to `${AIRFLOW_SITE_REPO}/docs-archive/<version>/`

    ```bash
    mkdir -p "${AIRFLOW_SITE_REPO}/docs-archive/${AIRFLOW_VERSION}"
    cp -r "${AIRFLOW_REPO}/docs/_build/html/." "${AIRFLOW_SITE_REPO}/docs-archive/${AIRFLOW_VERSION}"
    ```

    You can also mark the release as the latest stable version:

    ```bash
    echo "${AIRFLOW_VERSION}" > "${AIRFLOW_SITE_REPO}/docs-archive/stable.txt"
    ```

4.  Make a commit with generated documentation only.

    ```bash
    cd "${AIRFLOW_SITE_REPO}" && git checkout -b "docs-for-${AIRFLOW_VERSION}"
    cd "${AIRFLOW_SITE_REPO}" && git add .
    cd "${AIRFLOW_SITE_REPO}" && git commit -m "Docs for ${AIRFLOW_VERSION}"
    ```
5. To send changes to the remote server:

    ```bash
    cd "${AIRFLOW_SITE_REPO}" && git push origin "docs-for-${AIRFLOW_VERSION}"
    ```

# Publish site on Apache server

In order to push changes to the WWW server you need to have the two copy of `apache/airflow-site` repository. The first contains `master` branch checkoued, the second - `asf-site`.

## Prerequisite tasks

You should install and set up all software from "Working with the project/Prerequisite tasks" section.

The next steps will assume that these variable are available.
```bash
AIRFLOW_SITE_REPO=$HOME/airflow-site
AIRFLOW_SITE_ASF_SITE_REPO=$HOME/airflow-site-asf-site
```

To clone repository run following commands:
```bash
git clone git@github.com:apache/airflow-site.git "${AIRFLOW_SITE_REPO}"
git clone git@github.com:apache/airflow-site.git "${AIRFLOW_SITE_ASF_SITE_REPO}"

cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git checkout asf-site
cd "${AIRFLOW_SITE_REPO}" && git submodule update --init --recursive
```

*Known issues:*

Git worktree does not work properly with repositories that have submodules. Therefore, do not use this features and make multiple full copies of the repositories.

## Instruction

1. To run build site, run following commnad

    ```bash
    cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-landing-pages
    cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-site
    ```

2. Remove all files from `asf-site` branch

    ```bash
    cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git ls-files | xargs -P 16 rm -rf
    ```

3. Copy new release

    ```bash
    cp -vr "${AIRFLOW_SITE_REPO}/dist/." "${AIRFLOW_SITE_ASF_SITE_REPO}"
    ```

4. Commit changes

    ```bash
    cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git add .
    cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git commit -m "Update - $(date)"
    ```

5. Push changess

    ```bash
    cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git push origin asf-site
    ```

# Release and publish documentation in one go

###  Prerequisite tasks

You must have the software discussed in "Working with the project/Prerequisite tasks" and  "How to release new documentation" section installed.

### Instrucction

It is necessary to configure 3 variables that point to directories with repositories and one that describe current Airflow version. The next steps will assume that these variables are available.
```bash
AIRFLOW_REPO=$HOME/airflow
AIRFLOW_SITE_REPO=$HOME/airflow-site
AIRFLOW_SITE_REPO_ASF_SITE=$HOME/airflow-site
AIRFLOW_VERSION=1.10.9
```

Run following commands to do a lot of magic in one go.
```bash
# Clone repository
git clone git@github.com:apache/airflow.git "${AIRFLOW_REPO}"
cd "${AIRFLOW_REPO}" && git checkout "${AIRFLOW_VERSION}"
git clone git@github.com:apache/airflow-site.git "${AIRFLOW_SITE_REPO}"
cd "${AIRFLOW_SITE_REPO}" && git submodule update --init --recursive
cd "${AIRFLOW_SITE_REPO}" && git checkout -b "docs-${AIRFLOW_VERSION}"
git clone git@github.com:apache/airflow-site.git "${AIRFLOW_SITE_ASF_SITE_REPO}"
cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git checkout asf-site

# Install Python dependencies for Airflow
cd "${AIRFLOW_REPO}" && git checkout 1.10.9 && pip3 install  -e .[doc]

# Build image for site environment
cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-image

# Install themes
cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-site
cd "${AIRFLOW_SITE_REPO}" && bash site.sh prepare-theme
cd "${AIRFLOW_SITE_REPO}/sphinx_airflow_theme/" && pip3 install -e .

# Build docs
cd "${AIRFLOW_REPO}/docs/" && bash build.sh

# Copy docs
rm -rf "${AIRFLOW_SITE_REPO}/docs-archive/${AIRFLOW_VERSION}"
mv "${AIRFLOW_REPO}/docs/_build/html" "${AIRFLOW_SITE_REPO}/docs-archive/${AIRFLOW_VERSION}"

# Set current version as stable
echo "${AIRFLOW_VERSION}" > "${AIRFLOW_SITE_REPO}/docs-archive/stable.txt"

# Create commit
cd "${AIRFLOW_SITE_REPO}" && git add .
cd "${AIRFLOW_SITE_REPO}" && git commit -m 'Docs for ${AIRFLOW_VERSION}'

# Push new documentation
cd "${AIRFLOW_SITE_REPO}" && git push origin origin
```

When it is accepted and merged, then run following commandss:

```bash
# Fetch changes
cd "${AIRFLOW_SITE_REPO}" && git fetch
cd "${AIRFLOW_SITE_REPO}" && git checkout master && git reset --hard origin/master

# Build fresh landing pages and site
cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-landing-pages
cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-site

# Remove all files from `asf-site` branch
cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git ls-files | xargs -P 16 rm -rf

# Copy files to asf-site branch
cp -vr "${AIRFLOW_SITE_REPO}/dist/." "${AIRFLOW_SITE_ASF_SITE_REPO}/"

# Create commit
cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git add .
cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git commit -m "Update - $(date)"

# Push new website
cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git push origin asf-site
```

# Additional tips:

## Using VM on GCP

You should set following variable:
```bash
GCP_ZONE="europe-west3-b"
GCP_INSTANCE_NAME="test-airflow-docs-build"
```

If you want to create VM on GCP, you could use following command:
```bash
gcloud compute instances create "${GCP_INSTANCE_NAME}" \
    --custom-memory=32GB \
    --custom-cpu=6 \
    --zone="${GCP_ZONE}" \
    --image-family="debian-10" \
    --image-project="debian-cloud"
```

To connect via SSH and forward local SSH key to VM, forwardd ports from VM run following command:
```bash
gcloud beta compute \
       ssh \
       --zone "${GCP_ZONE}" \
       "${GCP_INSTANCE_NAME}" \
       -- \
       -A \
       -L "8000:127.0.0.1:8000" \
       -L "3000:127.0.0.1:3000" \
       -L "1313:127.0.0.1:1313"
```

To delete VM, run following command:
```bash
gcloud compute instances delete "${GCP_INSTANCE_NAME}"  --zone="${GCP_ZONE}"
```

## Use RAM disk for build

If you wanna create RAM disk, run following command:
```bash
sudo mkdir -p /mnt/ramdisk && sudo mount -t tmpfs -o size=16g tmpfs /mnt/ramdisk
```

To force Python to use RAM disk, run following command:
```bash
rm -rf $HOME/.local/lib/python3.7
mkdir -p $HOME/.local/lib/
mkdir -p /mnt/ramdisk/python3.7
ln -s  /mnt/ramdisk/python3.7 $HOME/.local/lib/python3.7
```

All environment variable used in guide should look as following:
```
AIRFLOW_REPO=/mnt/ramdisk/airflow
AIRFLOW_SITE_REPO=/mnt/ramdisk/airflow-site
AIRFLOW_SITE_ASF_SITE_REPO=/mnt/ramdisk/airflow-site-asf-site
```
