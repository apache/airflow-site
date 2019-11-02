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

IMAGE_NAME=airflow-site
CONTAINER_NAME=airflow-site-c

function usage {
cat << EOF
usage: ${0} <command> [<args>]

These are  ${0} commands used in various situations:

    stop               Stop the environment
    build-image        Build a Docker image with a environment
    install-node-deps  Download all the Node dependencies
    preview            Starts the web server
    build-site         Builds a website
    lint-css           Lint CSS files
    lint-js            Lint Javascript files
    shell              Start shell
    help               Display usage

Unrecognized commands are run as programs in the container.

For example, if you want to display a list of files, you
can execute the following command:

    $0 ls

EOF
}

function ensure_image_exists {
    if [[ ! $(docker images "${IMAGE_NAME}" -q) ]]; then
        echo "Image not exists."
        build_image
    fi
}

function ensure_container_exists {
    if [[ ! $(docker container ls -a --filter="Name=${CONTAINER_NAME}" -q ) ]]; then
        echo "Container not exists"
        docker run \
            --detach \
            --name "${CONTAINER_NAME}" \
            --volume "$(pwd):/opt/site/" \
            --publish 1313:1313 \
            --publish 3000:3000 \
            "${IMAGE_NAME}" sh -c 'trap "exit 0" INT; while true; do sleep 30; done;'
        return 0
    fi
}

function ensure_container_running {
    container_status="$(docker inspect "${CONTAINER_NAME}" --format '{{.State.Status}}')"
    echo "Current container status: ${container_status}"
    if [[ ! "${container_status}" == "running" ]]; then
        echo "Container not running. Starting the container."
        docker start "${CONTAINER_NAME}"
    fi
}

function ensure_node_module_exists {
    if [[ ! -d landing-pages/node_modules/ ]] ; then
        echo "Missing node dependencies. Start installation."
        docker exec -w "/opt/site/landing-pages/" "${CONTAINER_NAME}" yarn install
        echo "Dependencies installed."
    fi
}

function build_image {
    echo "Start building image"
    docker build -t airflow-site .
    echo "End building image"
}

if [[ "$#" -eq 0 ]]; then
    echo "You must provide at least one command."
    echo
    usage
    exit 1
fi

CMD=$1

shift

# Check fundamentals commands
if [[ "${CMD}" == "build-image" ]] ; then
    build_image
    exit 0
elif [[ "${CMD}" == "stop" ]] ; then
    docker kill "${CONTAINER_NAME}"
    exit 0
elif [[ "${CMD}" == "help" ]]; then
    usage
    exit 0
fi

ensure_image_exists
ensure_container_exists
ensure_container_running

# Check container commands
if [[ "${CMD}" == "install-node-deps" ]] ; then
    docker exec -w "/opt/site/landing-pages/" "${CONTAINER_NAME}" yarn install
elif [[ "${CMD}" == "preview" ]]; then
    ensure_node_module_exists
    docker exec -w "/opt/site/landing-pages/" "${CONTAINER_NAME}" npm run preview
elif [[ "${CMD}" == "build-site" ]]; then
    ensure_node_module_exists
    docker exec -w "/opt/site/landing-pages/" "${CONTAINER_NAME}" npm run build
elif [[ "${CMD}" == "lint-js" ]]; then
    ensure_node_module_exists
    docker exec -w "/opt/site/landing-pages/" "${CONTAINER_NAME}" npm run lint:js
elif [[ "${CMD}" == "lint-css" ]]; then
    ensure_node_module_exists
    docker exec -w "/opt/site/landing-pages/" "${CONTAINER_NAME}" npm run lint:css
elif [[ "${CMD}" == "shell" ]]; then
    docker exec -ti "${CONTAINER_NAME}" bash
else
    docker exec -ti "${CONTAINER_NAME}" "${CMD}" "$@"
fi

popd &>/dev/null || exit 1
