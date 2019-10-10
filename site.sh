#!/usr/bin/env bash

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

set -euox pipefail

MY_DIR="$(cd "$(dirname "$0")" && pwd)"
pushd "${MY_DIR}" &>/dev/null || exit 1

function check_image_exists {
    if docker images | tail -n +2 | cut -d " " -f 1 | sort | uniq | grep "$1" > /dev/null; then
        return 0
    fi
    return 1
}

function usage {
cat << EOF
usage: ${0} <command> [<args>]

These are  ${0} commands used in various situations:

    build-image        Build a Docker image with a  environment
    install-node-deps  Download all the Node dependencies
    preview            Starts the web server
    build-site         Builds a website
    lint-js            Lint all javascript files
    shell              Start shell.
    help               Display usage

Unrecognized commands are run as programs in the container.

For example, if you want to display a list of files, you
can execute the following command:

    $0 ls

EOF
}

function ensure_image_exists {
    if ! check_image_exists "airflow-site"; then
        echo "Image not exists."
        build_image
    fi
}

function ensure_node_module_exists {
    if [[ ! -d landing-pages/node_modules/ ]] ; then
        echo "Missing node depedencies. Start installation."
        start_container bash -c "cd landing-pages/ && yarn install"
        echo "Dependencies installed"
    fi
}

function build_image {
    echo "Start building image"
    docker build -t airflow-site .
    echo "End building image"
}

function start_container {
    ensure_image_exists

    docker run -ti \
        -v "$(pwd):/opt/site/" \
        -p 1313:1313 \
        -p 3000:3000 \
        airflow-site "$@"
}

if [[ "$#" -ge 1 ]] ; then
    if [[ "$1" == "build-image" ]] ; then
        build_image
    elif [[ "$1" == "install-node-deps" ]] ; then
        start_container bash -c "cd landing-pages/ && yarn install"
    elif [[ "$1" == "preview" ]]; then
        ensure_node_module_exists
        start_container bash -c "cd landing-pages/site && npm run preview"
    elif [[ "$1" == "build-site" ]]; then
        ensure_node_module_exists
        start_container bash -c "cd landing-pages/site && npm run build"
    elif [[ "$1" == "lint-js" ]]; then
        ensure_node_module_exists
        start_container bash -c "cd landing-pages/site && npm run lint"
    elif [[ "$1" == "shell" ]]; then
        start_container "bash"
    elif [[ "$1" == "help" ]]; then
        usage
    else
        start_container "$@"
    fi
else
    usage
fi

popd &>/dev/null || exit 1
