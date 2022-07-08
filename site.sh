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
pushd "${MY_DIR}" &>/dev/null || exit 1

IMAGE_NAME=airflow-site
CONTAINER_NAME=airflow-site-c

function log {
    echo -e "$(date +'%Y-%m-%d %H:%M:%S'):INFO: ${*} " >&2;
}

function usage {
cat << EOF
usage: ${0} <command> [<args>]

These are  ${0} commands used in various situations:

    build-site            Prepare dist directory with landing pages and documentation.
    preview-landing-pages Starts the web server with preview of the website.
    build-landing-pages   Builds a landing pages.
    prepare-theme         Prepares and copies files needed for the proper functioning of the sphinx theme.
    shell                 Start shell.
    build-image           Build a Docker image with a environment.
    install-node-deps     Download all the Node dependencies.
    check-site-links      Checks if the links are correct in the website.
    lint-css              Lint CSS files.
    lint-js               Lint Javascript files.
    cleanup               Delete the virtual environment in Docker.
    stop                  Stop the environment.
    help                  Display usage.

Unrecognized commands are run as programs in the container.

For example, if you want to display a list of files, you
can execute the following command:

    $0 ls

The following command can also be performed from the Docker environment:
install-node-deps, preview, build-site, lint-css, lint-js.

The lint-css and lint-js accept paths in arguments. If no path is given, the script
will be executed for all supported files.

EOF
}

function ensure_image_exists {
    log "Checking if image exists: ${IMAGE_NAME}"
    if [[ ! $(docker images "${IMAGE_NAME}" -q) ]]; then
        log "Image not exists."
        build_image
    fi
}

function ensure_container_exists {
    log "Checking if container exists: ${CONTAINER_NAME}"
    if [[ ! $(docker container ls -a --filter="Name=${CONTAINER_NAME}" -q ) ]]; then
        log "Container not exists"
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
    log "Checking if container running: ${CONTAINER_NAME}"
    container_status="$(docker inspect "${CONTAINER_NAME}" --format '{{.State.Status}}')"
    log "Current container status: ${container_status}"
    if [[ ! "${container_status}" == "running" ]]; then
        log "Container not running. Starting the container."
        docker start "${CONTAINER_NAME}"
    fi
}

function ensure_node_module_exists {
    log "Checking if node module exists"
    if [[ ! -d landing-pages/node_modules/ ]] ; then
        log "Missing node dependencies. Start installation."
        run_command "/opt/site/landing-pages/" yarn install
        log "Dependencies installed."
    fi
}

function ensure_that_website_is_build {
    log "Check if landing-pages/dist/index.html file exists"
    if [[ ! -f landing-pages/dist/index.html ]] ; then
        log "The website is not built. Start building."
        run_command "/opt/site/landing-pages/" npm run build
        log "The website builded."
    fi
}

function build_image {
    log "Start building image"
    docker build -t airflow-site .
    log "End building image"
}

function run_command {
    log "Running command: $*"
    working_directory=$1
    shift
    if [[ -f /.dockerenv ]] ; then
        pushd "${working_directory}"
        exec "$@"
    else
        if ! test -t 0; then
            docker exec \
                --interactive \
                --workdir "${working_directory}" \
                "${CONTAINER_NAME}" "$@"
        else
            docker exec \
                --tty \
                --interactive \
                --workdir "${working_directory}" \
                "${CONTAINER_NAME}" "$@"
        fi
    fi
}

function prepare_environment {
    log "Preparing environment"
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

    DOCKER_PATHS=()
    for E in "${@}"; do
        ABS_PATH=$(cd "${WORKING_DIR}" && realpath "${E}")
        DOCKER_PATHS+=("/opt/site/$(relativepath "$(pwd)" "${ABS_PATH}")")
    done
    run_command "${script_working_directory}" "${command}" "${DOCKER_PATHS[@]}"
}

function prepare_packages_metadata {
    log "Preparing packages-metadata.json"
    python3 dump-docs-packages-metadata.py > "landing-pages/site/static/_gen/packages-metadata.json"
}

function build_landing_pages {
    log "Building landing pages"
    run_command "/opt/site/landing-pages/" npm run index
    prepare_packages_metadata
    run_command "/opt/site/landing-pages/" npm run build
}

function create_redirect {
    output_file="$1"
    target_location="$2"
    log "Creating redirect: ${output_file} => ${target_location}"

    cat > "${output_file}" <<EOF
<!DOCTYPE html>
<html>
   <head><meta http-equiv="refresh" content="1; url=${target_location}" /></head>
   <body></body>
</html>
EOF
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

    if [[ ! -f "landing-pages/dist/index.html" ]]; then
        build_landing_pages
    fi
    mkdir -p dist
    rm -rf dist/*
    verbose_copy landing-pages/dist/. dist/
    for pkg_path in docs-archive/*/ ; do
        # Process directories only,
        if [ ! -d "${pkg_path}" ]; then
            continue;
        fi

        package_name="$(basename -- "${pkg_path}")"

        # Is this documentation versioned?
        if [ -f "${pkg_path}/stable.txt" ]; then
            mkdir -p "docs-archive/${package_name}"
            for ver_path in "docs-archive/${package_name}"/*/ ; do
                version="$(basename -- "${ver_path}")"
                verbose_copy "docs-archive/${package_name}/${version}/." "dist/docs/${package_name}/${version}"
            done
            stable_version="$(cat "docs-archive/${package_name}/stable.txt")"
            verbose_copy "docs-archive/${package_name}/${stable_version}/." "dist/docs/${package_name}/stable"
            create_redirect "dist/docs/${package_name}/index.html" "/docs/${package_name}/stable/index.html"
        else
            verbose_copy "docs-archive/${package_name}/." "dist/docs/${package_name}/"
        fi
    done
    # This file may already have been created during building landing pages,
    # but when building a full site, it's worth regenerate
    log "Preparing packages-metadata.json"
    python3 dump-docs-packages-metadata.py > "dist/_gen/packages-metadata.json"

    # Sanity checks
    assert_file_exists dist/docs/index.html
    assert_file_exists dist/docs/apache-airflow/index.html
    assert_file_exists dist/docs/apache-airflow/1.10.7/tutorial.html
    assert_file_exists dist/docs/apache-airflow/stable/tutorial.html
    assert_file_exists dist/_gen/packages-metadata.json
}

function cleanup_environment {
    container_status="$(docker inspect "${CONTAINER_NAME}" --format '{{.State.Status}}')"
    log "Current container status: ${container_status}"
    if [[ "${container_status}" == "running" ]]; then
        log "Container running. Killing the container."
        docker kill "${CONTAINER_NAME}"
    fi

    if [[ $(docker container ls -a --filter="Name=${CONTAINER_NAME}" -q ) ]]; then
        log "Container exists. Removing the container."
        docker rm "${CONTAINER_NAME}"
    fi

    if [[ $(docker images "${IMAGE_NAME}" -q) ]]; then
        log "Images exists. Deleting the image."
        docker rmi "${IMAGE_NAME}"
    fi
}

function prepare_theme {
    log "Preparing theme files"
    SITE_DIST="landing-pages/dist"
    THEME_GEN="sphinx_airflow_theme/sphinx_airflow_theme/static/_gen"
    mkdir -p "${THEME_GEN}/css" "${THEME_GEN}/js"
    cp ${SITE_DIST}/docs.*.js "${THEME_GEN}/js/docs.js"
    cp ${SITE_DIST}/scss/main.min.*.css "${THEME_GEN}/css/main.min.css"
    cp ${SITE_DIST}/scss/main-custom.min.*.css "${THEME_GEN}/css/main-custom.min.css"
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

# Check fundamentals commands
if [[ "${CMD}" == "build-image" ]] ; then
    prevent_docker
    build_image
    exit 0
elif [[ "${CMD}" == "stop" ]] ; then
    prevent_docker
    docker kill "${CONTAINER_NAME}"
    exit 0
elif [[ "${CMD}" == "cleanup" ]] ; then
    prevent_docker
    cleanup_environment
    exit 0
elif [[ "${CMD}" == "help" ]]; then
    usage
    exit 0
fi

prepare_environment

# Check container commands
if [[ "${CMD}" == "install-node-deps" ]] ; then
    run_command "/opt/site/landing-pages/" yarn install
elif [[ "${CMD}" == "preview-landing-pages" ]]; then
    ensure_node_module_exists
    run_command "/opt/site/landing-pages/" npm run index
    prepare_packages_metadata
    run_command "/opt/site/landing-pages/" npm run preview
elif [[ "${CMD}" == "build-landing-pages" ]]; then
    ensure_node_module_exists
    build_landing_pages
elif [[ "${CMD}" == "build-site" ]]; then
    ensure_node_module_exists
    build_site
elif [[ "${CMD}" == "check-site-links" ]]; then
    ensure_node_module_exists
    ensure_that_website_is_build
    run_command "/opt/site/landing-pages/" ./check-links.sh
elif [[ "${CMD}" == "prepare-theme" ]]; then
    ensure_that_website_is_build
    prepare_theme
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
