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

# Pre-commit hook that checks if sphinx_airflow_theme files have changed.
# If they have, it bumps the patch version and updates the stored hash.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
THEME_DIR="${REPO_ROOT}/sphinx_airflow_theme"
THEME_MODULE="${THEME_DIR}/sphinx_airflow_theme"
HASH_FILE="${THEME_DIR}/.theme_files_hash"
VERSION_FILE="${THEME_DIR}/LATEST_VERSION.txt"
INIT_FILE="${THEME_MODULE}/__init__.py"

compute_theme_hash() {
    # Hash all theme files (excluding version lines in __init__.py) plus pyproject.toml.
    # We use shasum via stdin (< "$f") to avoid embedding absolute paths in the hash.
    # File paths are echoed separately so the hash is stable regardless of working directory.
    (
        find "${THEME_MODULE}" -type f | sort | while read -r f; do
            local relative
            relative="${f#"${REPO_ROOT}/"}"
            if [ "$f" = "${INIT_FILE}" ]; then
                echo "${relative}"
                grep -v '^__version__' "$f" | grep -v '^__version_full__' | shasum -a 256 | cut -d' ' -f1
            else
                echo "${relative}"
                shasum -a 256 < "$f" | cut -d' ' -f1
            fi
        done
        echo "sphinx_airflow_theme/pyproject.toml"
        shasum -a 256 < "${THEME_DIR}/pyproject.toml" | cut -d' ' -f1
    ) | shasum -a 256 | cut -d' ' -f1
}

current_hash=$(compute_theme_hash)

if [ -f "${HASH_FILE}" ]; then
    stored_hash=$(head -1 "${HASH_FILE}" | tr -d '[:space:]')
else
    stored_hash=""
fi

if [ "${current_hash}" = "${stored_hash}" ]; then
    # No changes, verify version file is in sync
    current_version=$(grep '^__version__' "${INIT_FILE}" | head -1 | sed "s/.*= *['\"]//;s/['\"]//")
    stored_version=$(head -1 "${VERSION_FILE}" | tr -d '[:space:]')
    if [ "${current_version}" != "${stored_version}" ]; then
        echo "${current_version}" > "${VERSION_FILE}"
        git add "${VERSION_FILE}"
        echo "sphinx_airflow_theme: synced LATEST_VERSION.txt to ${current_version}"
    fi
    exit 0
fi

# Hash changed - bump the patch version
current_version=$(grep '^__version__' "${INIT_FILE}" | head -1 | sed "s/.*= *['\"]//;s/['\"]//")
IFS='.' read -r major minor patch <<< "${current_version}"
new_patch=$((patch + 1))
new_version="${major}.${minor}.${new_patch}"

echo "sphinx_airflow_theme: files changed, bumping version ${current_version} -> ${new_version}"

# Update __init__.py
sed -i.bak "s/^__version__ = .*/__version__ = '${new_version}'/" "${INIT_FILE}"
sed -i.bak "s/^__version_full__ = .*/__version_full__ = __version__/" "${INIT_FILE}"
rm -f "${INIT_FILE}.bak"

# Recompute hash after version bump (since __init__.py changed but version lines are excluded)
new_hash=$(compute_theme_hash)

# Update stored hash and version
echo "${new_hash}" > "${HASH_FILE}"
echo "${new_version}" > "${VERSION_FILE}"

# Stage the modified files
git add "${INIT_FILE}" "${HASH_FILE}" "${VERSION_FILE}"

echo "sphinx_airflow_theme: updated hash and version files"
exit 1
