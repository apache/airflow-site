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
* docker (for the shell language linter)
* Node 16
* Yarn
* Hugo

It is also worth adding SSH keys for the `github.com` server to trusted ones. It is necessary to clone repositories. You can do this using following command:
```bash
ssh-keyscan -t rsa -H github.com >> ~/.ssh/known_hosts
```

**Debian installation**

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

To install Node 16, first install the [Node version manager](https://github.com/nvm-sh/nvm), `nvm`. Then, install Node 16 with these commands:

```bash
nvm install 16
nvm use 16
```

To install yarn, run the following command:
```bash
npm install -g yarn
```

To install hugo on Debian, run the following command:
```bash
sudo apt install hugo -y
```

**macOS installation**

To install git on macOS, install the XCode Command Line Tools with the following command:
```bash
xcode-select --install
```

Then, install [Homebrew](https://brew.sh). Once that has completed, you can install Hugo:
```bash
brew install hugo
```

To install Node 16, first install the [Node version manager](https://github.com/nvm-sh/nvm), `nvm`. Then, install Node 16 with these commands:

```bash
nvm install 16
nvm use 16
```

To install Yarn, run the following command:
```bash
brew install yarn
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

In order to manage your local environment for the project, use the `site.sh` script.

`site.sh` provides the following commands.

    build-site            Prepare dist directory with landing pages and documentation
    preview-landing-pages Starts the web server with preview of the website
    build-landing-pages   Builds a landing pages
    prepare-theme         Prepares and copies files needed for the proper functioning of the sphinx theme.
    install-node-deps     Download all the Node dependencies
    check-site-links      Checks if the links are correct in the website
    lint-css              Lint CSS files
    lint-js               Lint Javascript files
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

### How to add a blog post with images

In order to add a new blog post with images, you need to add it in sub-folder of the "blog" folder and
name your markdown file "index.md". Images placed  in this folder can be referred to directly from
the markdown file using this directive:

```markdown
![Alt text](image.png)
```

### How to add a new company testimonial

To add a new company testimonials with pre-filled frontmatter, in `<ROOT DIRECTORY>/landing-pages/site` run:
```bash
hugo new testimonials/my-testimonial.md
```

That will create a markdown file `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/testimonials/my-testimonial.md`
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
blocktype: testimonial
---

##### What was the problem?
text

##### How did Apache Airflow help to solve this problem?
text

##### What are the results?
text
```
When you finish your testimonial, remember to **remove `draft: true`** from frontmatter.

---

To add a new testimonial manually, create a markdown file in `<ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/testimonials/<filename>.md`.
The filename will also serve as URL for the testimonial.

Then, **at the top of the file**, add frontmatter in following format:

```
---
title: "<testimonial title>"
linkTitle: "<testimonial link title>"
quote:
    text: "<quote text>"
    author: "<quote author's name>"
logo: "<logo filename (with extension)>"
blocktype: testimonial
---
```
Below frontmatter, put your testimonial content in the following format:

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

Path to logo file: <ROOT DIRECTORY>/landing-pages/site/static/usecase-logos/my-testimonial.svg

Testimonial in <ROOT DIRECTORY>/landing-pages/site/content/<LANGUAGE VERSION>/use-cases/my-testimonial.md

```
---
title: "<testimonial title>"
linkTitle: "<testimonial link title>"
quote:
    text: "<quote text>"
    author: "<quote author's name>"
logo: "my-testimonial.svg"
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

### Preview changes on pull requests (CI/CD)

1. Github Action has been configured to automatically publish artifacts for pull requests, so we can preview changes from Github Ui.
  ![](https://docs.github.com/assets/images/help/repository/passing-data-between-jobs-in-a-workflow.png)

2. After downloading the artifacts, unpack the archive and start the local HTTP server, run the following command.

  Python 3
  ```bash
  python -m http.server --cgi 8000
  ```
  Python 2.7
  ```bash
  python -m SimpleHTTPServer 8000
  ```


# How to release new documentation

Building documentation for the Apache Airlfow project also requires Python3.6 with pip and graphviz. You also need to have additional `apache/airflow` repository available.

### Prerequisite Tasks

You should install and set up all software from "Working with the project/Prerequisite tasks" section.

The following additional application must be installed to use the project:

* python3.6 or newer
* pip
* graphviz

**Debian installation:**

To install graphviz, pip for Debian, run following commands:
```bash
sudo apt install graphviz python3-pip -y
```

You should also add `$HOME/.local/bin` to `$PATH`, run following command:
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

1.  To prepare and install Sphinx theme, run following commands:
    ```bash
    cd "${AIRFLOW_SITE_REPO}" && bash site.sh build-site
    cd "${AIRFLOW_SITE_REPO}" && bash site.sh prepare-theme
    cd "${AIRFLOW_SITE_REPO}/sphinx_airflow_theme" && pip3 install -e .
    ```
2.  To build documentation, run following commands:
    ```bash
    cd "${AIRFLOW_REPO}" && git checkout "${AIRFLOW_VERSION}"
    cd "${AIRFLOW_REPO}" && breeze build-docs'
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

# Publish site on Apache server (CI/CD)

Github Action has been configured to automatically publish artifacts for pull requests, so you can preview changes.

# Publish site on Apache server (manual way)

It is recommended to use Github Action to publish changes to the website, but in case of problems it is also possible to publish changes to the website manually.


## Prerequisite tasks

You should install and set up all software from "Working with the project/Prerequisite tasks" section.

The next steps will assume that these variable are available.
```bash
AIRFLOW_SITE_REPO=$HOME/airflow-site
AIRFLOW_SITE_ASF_SITE_REPO=$HOME/airflow-site-asf-site
```

You need to have the two copy of `apache/airflow-site` repository. The first contains `master` branch checked, the second - `asf-site`. To clone repository run following commands:
```bash
git clone git@github.com:apache/airflow-site.git "${AIRFLOW_SITE_REPO}"
git clone git@github.com:apache/airflow-site.git "${AIRFLOW_SITE_ASF_SITE_REPO}"

cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git checkout asf-site
cd "${AIRFLOW_SITE_REPO}" && git submodule update --init --recursive
```

*Known issues:*

Git worktree does not work properly with repositories that have submodules. Therefore, do not use this features and make multiple full copies of the repositories.

## Instruction

1. To run build site, run following command

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

5. Push changes

    ```bash
    cd "${AIRFLOW_SITE_ASF_SITE_REPO}" && git push origin asf-site
    ```

# Release and publish documentation in one go

###  Prerequisite tasks

You must have the software discussed in "Working with the project/Prerequisite tasks" and  "How to release new documentation" section installed.

### Instruction

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

Once it is accepted and merged, wait for Github Action build to publish the changes.

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

To connect via SSH and forward local SSH key to VM, forward ports from VM run following command:
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
