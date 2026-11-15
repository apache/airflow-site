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

FROM debian:bookworm-slim

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

RUN curl -sL https://deb.nodesource.com/setup_24.x | bash - \
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

RUN HUGOHOME="$(mktemp -d)" \
    && export HUGOHOME \
    && curl -fsSL https://github.com/gohugoio/hugo/releases/download/v0.170.0/hugo_0.170.0_linux-amd64.tar.gz > "${HUGOHOME}/hugo.tar.gz" \
    && echo "0930754ec22ad2dd1a252f8c31a5e57faccc9d15f1c3d381ddafcb96eeb8aef0  ${HUGOHOME}/hugo.tar.gz" | sha256sum -c - \
    && tar -xzvf "${HUGOHOME}/hugo.tar.gz" hugo \
    && mv hugo /usr/local/bin/hugo \
    && chmod +x /usr/local/bin/hugo \
    && rm -r "${HUGOHOME}"

# Docsy compiles its SCSS with Dart Sass. Expose it as `dart-sass`, which Hugo
# looks up before `sass`, so the pure-JS `sass` in node_modules/.bin can't shadow it.
RUN curl -fsSL -o /tmp/dart-sass.tar.gz https://github.com/sass/dart-sass/releases/download/1.108.2/dart-sass-1.108.2-linux-x64.tar.gz \
    && echo "32d2eb5b83cbc180fce9657ff3c57401a9006c59eccfe0bfdde0aa755a66d42f  /tmp/dart-sass.tar.gz" | sha256sum -c - \
    && tar -xzf /tmp/dart-sass.tar.gz -C /opt \
    && rm /tmp/dart-sass.tar.gz \
    && printf '#!/bin/sh\nexec /opt/dart-sass/sass "$@"\n' > /usr/local/bin/dart-sass \
    && chmod +x /usr/local/bin/dart-sass

WORKDIR /opt/site/
