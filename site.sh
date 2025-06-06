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
set -euo pipefail

WORKING_DIR="$(pwd)"
MY_DIR="$(cd "$(dirname "$0")" && pwd)"

function log {
    echo -e "$(date +'%Y-%m-%d %H:%M:%S'):INFO: ${*} " >&2;
}

function usage {
cat << EOF
usage: ${0} <command> [<args>]

These are the ${0} commands that can be used in various situations:

    build-site            Prepare dist/ directory with landing pages and docs.
    preview-landing-pages Start the web server with preview of the landing pages.
    build-landing-pages   Build the landing pages.
    prepare-theme         Copy required CSS/JS files from landing pages into the docs theme.
    install-node-deps     Download all the Node dependencies.
    check-site-links      Check to make sure that links are correct in the website.
    lint-css              Lint CSS files.
    lint-js               Lint Javascript files.
    help                  Display usage.

The lint-css and lint-js commands accept paths in arguments. If no path is given,
the script will be executed for all supported files.

EOF
}

function ensure_node_module_exists {
    log "Checking if node module exists"
    if [[ ! -d ${MY_DIR}/landing-pages/node_modules/ ]] ; then
        log "Missing node dependencies. Start installation."
        run_command "./landing-pages/" yarn install
        log "Dependencies installed."
    fi
}

function ensure_that_website_is_build {
    log "Check if ${MY_DIR}/landing-pages/dist/index.html file exists"
    if [[ ! -f ${MY_DIR}/landing-pages/dist/index.html ]] ; then
        log "The website is not built. Start building."
        run_command "${MY_DIR}/landing-pages/" yarn run build
        log "The website built."
    fi
}

function run_command {
    working_directory=$1
    shift
    log "Changing to ${working_directory} and running: $*@"
    pushd "${working_directory}" &>/dev/null || exit 1
    "$@"
    popd &>/dev/null || exit 1
}

function relativepath {
    source=$1
    target=$2

    common_part=$source # for now
    result="" # for now

    while [[ "${target#"$common_part"}" == "${target}" ]]; do
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
    forward_part="${target#"$common_part"}"

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

    MAPPED_PATHS=()
    for E in "${@}"; do
        ABS_PATH=$(cd "${WORKING_DIR}" && realpath "${E}")
        MAPPED_PATHS+=("${MY_DIR}/$(relativepath "$(pwd)" "${ABS_PATH}")")
    done
    run_command "${script_working_directory}" "${command}" "${MAPPED_PATHS[@]}"
}

function prepare_packages_metadata {
    log "Preparing packages-metadata.json"
    uv run "${MY_DIR}"/.github/scripts/dump-docs-packages-metadata.py > "${MY_DIR}/landing-pages/site/static/_gen/packages-metadata.json"
}

function build_landing_pages {
    log "Building landing pages"
    run_command "${MY_DIR}/landing-pages/" yarn run index
    prepare_packages_metadata
    run_command "${MY_DIR}/landing-pages/" yarn run build
}

function verbose_copy {
    source="$1"
    target="$2"
    log "Copying '$source' to '$target'"
    mkdir -p "${target}"
    cp -R "$source" "$target"
}

function assert_file_exists {
    file_path="$1"
    if [[ ! -f "${file_path}" ]]; then
        echo "Missing file: ${file_path}":
        exit 1
    fi
}

function build_site {
    log "Building full site"

    if [[ ! -f "${MY_DIR}/landing-pages/dist/index.html" ]]; then
        build_landing_pages
    fi

    pushd "${MY_DIR}" &>/dev/null || exit 1

    mkdir -p dist
    rm -rf dist/*
    verbose_copy landing-pages/dist/. dist/

    popd &>/dev/null || exit 1

    # This file may already have been created during building landing pages,
    # but when building a full site, it's worth regenerate
    log "Preparing packages-metadata.json"
    uv run "${MY_DIR}"/.github/scripts/dump-docs-packages-metadata.py > "${MY_DIR}/dist/_gen/packages-metadata.json"

    # Sanity checks
    assert_file_exists "${MY_DIR}"/dist/docs/index.html
    assert_file_exists "${MY_DIR}"/dist/_gen/packages-metadata.json
}

function prepare_theme {
    log "Preparing theme files"
    SITE_DIST="${MY_DIR}/landing-pages/dist"
    THEME_GEN="${MY_DIR}/sphinx_airflow_theme/sphinx_airflow_theme/static/_gen"
    mkdir -p "${THEME_GEN}/css" "${THEME_GEN}/js"
    cp "${SITE_DIST}"/docs.*.js "${THEME_GEN}/js/docs.js"
    cp "${SITE_DIST}"/scss/main.min.*.css "${THEME_GEN}/css/main.min.css"
    cp "${SITE_DIST}"/scss/main-custom.min.*.css "${THEME_GEN}/css/main-custom.min.css"
    echo "Successful copied required files"
}

if [[ "$#" -eq 0 ]]; then
    echo "You must provide at least one command."
    echo
    usage
    exit 1
fi

CMD=$1

shift

# Check commands
if [[ "${CMD}" == "install-node-deps" ]] ; then
    npm install --global yarn
    run_command "${MY_DIR}/landing-pages/" yarn install
elif [[ "${CMD}" == "preview-landing-pages" ]]; then
    ensure_node_module_exists
    run_command "${MY_DIR}/landing-pages/" yarn run index
    prepare_packages_metadata
    run_command "./landing-pages/" yarn run preview
elif [[ "${CMD}" == "build-landing-pages" ]]; then
    ensure_node_module_exists
    build_landing_pages
elif [[ "${CMD}" == "build-site" ]]; then
    ensure_node_module_exists
    build_site
elif [[ "${CMD}" == "check-site-links" ]]; then
    ensure_node_module_exists
    ensure_that_website_is_build
    run_command "${MY_DIR}/landing-pages/" ./check-links.sh
elif [[ "${CMD}" == "prepare-theme" ]]; then
    ensure_that_website_is_build
    prepare_theme
elif [[ "${CMD}" == "lint-js" ]]; then
    ensure_node_module_exists
    if [[ "$#" -eq 0 ]]; then
        run_command "${MY_DIR}/landing-pages/" yarn run lint:js
    else
        run_lint "${MY_DIR}/landing-pages/" ./node_modules/.bin/eslint "$@"
    fi
elif [[ "${CMD}" == "lint-css" ]]; then
    ensure_node_module_exists
    if [[ "$#" -eq 0 ]]; then
        run_command "${MY_DIR}/landing-pages/" yarn run lint:css
    else
        run_lint "${MY_DIR}/landing-pages/" ./node_modules/.bin/stylelint "$@"
    fi
else
    usage
    exit 0
fi
