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

WORKING_DIR="$(pwd)"
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

The following command can also be performed from the Docker environment:
install-node-deps, preview, build-site, lint-css, lint-js.

The lint-css and lint-js accept paths in arguments. If no path is given, the script
will be executed for all supported files

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
        run_command "/opt/site/landing-pages/" yarn install
        echo "Dependencies installed."
    fi
}

function build_image {
    echo "Start building image"
    docker build -t airflow-site .
    echo "End building image"
}

function run_command {
    working_directory=$1
    shift
    if [[ -f /.dockerenv ]] ; then
        echo "Native command"
        pushd "${working_directory}"
        exec "$@"
    else
        echo "Docker command"
        docker exec -w "${working_directory}" "${CONTAINER_NAME}" "$@"
    fi
}

function prepare_environment {
    if [[ ! -f /.dockerenv ]] ; then
        ensure_image_exists
        ensure_container_exists
        ensure_container_running
    fi
}

function prevent_docker {
    if [[ -f /.dockerenv ]] ; then
        echo "This command is not supported in the Docker environment. Run this command from the host system."
        exit 1
    fi
}

function relativepath {
    source=$1
    target=$2

    common_part=$source # for now
    result="" # for now

    while [[ "${target#$common_part}" == "${target}" ]]; do
        # no match, means that candidate common part is not correct
        # go up one level (reduce common part)
        common_part="$(dirname "$common_part")"
        # and record that we went back, with correct / handling
        if [[ -z $result ]]; then
            result=".."
        else
            result="../$result"
        fi
    done

    if [[ $common_part == "/" ]]; then
        # special case for root (no common path)
        result="$result/"
    fi

    # since we now have identified the common part,
    # compute the non-common part
    forward_part="${target#$common_part}"

    # and now stick all parts together
    if [[ -n $result ]] && [[ -n $forward_part ]]; then
        result="$result$forward_part"
    elif [[ -n $forward_part ]]; then
        # extra slash removal
        result="${forward_part:1}"
    fi
    echo "$result"
}

function run_lint {
    script_working_directory=$1
    command=$2
    shift 2

    DOCKER_PATHS=()
    for E in "${@}"; do
        ABS_PATH=$(cd "${WORKING_DIR}" && realpath "${E}")
        DOCKER_PATHS+=("/opt/site/$(relativepath "$(pwd)" "${ABS_PATH}")")
    done
    run_command "${script_working_directory}" "${command}" "${DOCKER_PATHS[@]}"
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
    prevent_docker
    build_image
    exit 0
elif [[ "${CMD}" == "stop" ]] ; then
    prevent_docker
    docker kill "${CONTAINER_NAME}"
    exit 0
elif [[ "${CMD}" == "help" ]]; then
    usage
    exit 0
fi

prepare_environment

# Check container commands
if [[ "${CMD}" == "install-node-deps" ]] ; then
    run_command "/opt/site/landing-pages/" yarn install
elif [[ "${CMD}" == "preview" ]]; then
    ensure_node_module_exists
    run_command "/opt/site/landing-pages/" npm run preview
elif [[ "${CMD}" == "build-site" ]]; then
    ensure_node_module_exists
    run_command "/opt/site/landing-pages/" npm run build
elif [[ "${CMD}" == "lint-js" ]]; then
    ensure_node_module_exists
    if [[ "$#" -eq 0 ]]; then
        run_command "/opt/site/landing-pages/" npm run lint:js
    else
        run_lint "/opt/site/landing-pages/" ./node_modules/.bin/eslint "$@"
    fi
elif [[ "${CMD}" == "lint-css" ]]; then
    ensure_node_module_exists
    if [[ "$#" -eq 0 ]]; then
        run_command "/opt/site/landing-pages/" npm run lint:css
    else
        run_lint "/opt/site/landing-pages/" ./node_modules/.bin/stylelint "$@"
    fi
elif [[ "${CMD}" == "shell" ]]; then
    prevent_docker
    docker exec -ti "${CONTAINER_NAME}" bash
else
    prevent_docker
    docker exec -ti "${CONTAINER_NAME}" "${CMD}" "$@"
fi

popd &>/dev/null || exit 1
