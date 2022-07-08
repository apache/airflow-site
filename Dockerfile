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

#
# The first stage builds golang and hugo from source
#

FROM debian:buster-slim as hugobuilder

RUN apt-get update \
     && apt-get install -y --no-install-recommends \
         build-essential \
         git \
         golang \
         ca-certificates \
         curl \
     && apt-get autoremove -yqq --purge \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/hugo

# Use the golang bin we just built to make an extended hugo binary
RUN curl -sL https://github.com/gohugoio/hugo/archive/refs/tags/v0.58.3.tar.gz > hugo.tar.gz \
     && tar --strip-components 1 -zxf hugo.tar.gz \
     && export GOPATH=/root/go && mkdir $GOPATH \
     && CGO_ENABLED=1 go install --tags extended

#
# The second stage is the website build image
#

FROM debian:buster-slim

SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    LANGUAGE=C.UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    LC_CTYPE=C.UTF-8 \
    LC_MESSAGES=C.UTF-8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        gnupg2 \
        gosu \
        lynx \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        nodejs \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends yarn \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL "https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64" > /usr/local/bin/jq \
    && chmod +x /usr/local/bin/jq

# Copy the extended Hugo binary from stage 1
COPY --from=hugobuilder /root/go/bin/hugo /usr/local/bin/hugo
RUN chmod +x /usr/local/bin/hugo

WORKDIR /opt/site/
