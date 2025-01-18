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

FROM python:3.9-slim

SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    LANGUAGE=C.UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    LC_CTYPE=C.UTF-8 \
    LC_MESSAGES=C.UTF-8

# Update and install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        git \
        gnupg2 \
        gosu \
        lynx \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js for potential front-end dependencies
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        nodejs \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Yarn for package management
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends yarn \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install jq for JSON processing (if needed in your Python scripts)
RUN curl -sL "https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64" > /usr/local/bin/jq \
    && chmod +x /usr/local/bin/jq

# Install Hugo for static site generation (if relevant for the project)
RUN HUGOHOME="$(mktemp -d)" \
    && export HUGOHOME \
    && curl -sL https://github.com/gohugoio/hugo/releases/download/v0.58.3/hugo_extended_0.58.3_Linux-64bit.tar.gz > "${HUGOHOME}/hugo.tar.gz" \
    && tar -xzvf "${HUGOHOME}/hugo.tar.gz" hugo \
    && mv hugo /usr/local/bin/hugo \
    && chmod +x /usr/local/bin/hugo \
    && rm -r "${HUGOHOME}"

# Set working directory for the Python site
WORKDIR /opt/site

# Copy the Python application files into the container
COPY . /opt/site/

# Install Python dependencies (assuming there's a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Python app (site.py)
CMD ["python", "site.py"]
