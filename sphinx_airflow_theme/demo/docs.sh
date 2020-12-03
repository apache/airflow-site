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

SOURCE_DIR="."
BUILD_DIR="${MY_DIR}/_build"
RELEASE_VERSION="2.0.0"

function usage {
cat << EOF
usage: ${0} <command> [<args>]

These are  ${0} commands used in various situations:

    build              Build the documentation
    preview            Build a Docker image with a environment
    help               Display usage

EOF
}

function build_sphinx_demo {
    echo "Starting build documentation"
    # -E  don't use a saved environment, always read all files
    # -T  show full traceback on exception
    # -d  path for the cached environment and doctree files
    sphinx-build \
        -E \
        -T \
        -d "_doctrees" \
        "${SOURCE_DIR}" "${BUILD_DIR}/docs/apache-airflow/${RELEASE_VERSION}"
}

function ensure_that_documentation_is_built {
    if [[ ! -f "_build/docs/apache-airflow/${RELEASE_VERSION}/index.html" ]] ; then
        echo "Documentation is not built."
        build_sphinx_demo
    fi
}

function start_preview {
    ensure_that_documentation_is_built
    (cd "${BUILD_DIR}/"; python -m http.server --cgi 3001)
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
if [[ "${CMD}" == "build" ]] ; then
    rm -rf _build
    build_sphinx_demo
    mkdir -p _build/_gen/
    (cd ../../; python dump-docs-packages-metadata.py > "${BUILD_DIR}/_gen/packages-metadata.json")
    exit 0
elif [[ "${CMD}" == "preview" ]] ; then
    start_preview
    exit 0
else
    usage
    exit 0
fi


popd &>/dev/null || exit 1
