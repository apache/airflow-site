#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.10"
# ///
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
"""Pre-commit hook that checks if sphinx_airflow_theme files have changed.

If they have, it bumps the patch version and updates the stored hash.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(
    subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
)
THEME_DIR = REPO_ROOT / "sphinx_airflow_theme"
THEME_MODULE = THEME_DIR / "sphinx_airflow_theme"
HASH_FILE = THEME_DIR / ".theme_files_hash"
VERSION_FILE = THEME_DIR / "LATEST_VERSION.txt"
INIT_FILE = THEME_MODULE / "__init__.py"


def compute_theme_hash() -> str:
    """Hash all theme files (excluding version lines in __init__.py) plus pyproject.toml.

    File paths are included as relative paths so the hash is stable regardless of working directory.
    """
    h = hashlib.sha256()
    for f in sorted(THEME_MODULE.rglob("*")):
        if not f.is_file():
            continue
        relative = f.relative_to(REPO_ROOT)
        h.update(f"{relative}\n".encode())
        if f == INIT_FILE:
            content = "".join(
                line
                for line in f.read_text().splitlines(keepends=True)
                if not line.startswith("__version__") and not line.startswith("__version_full__")
            )
            h.update(hashlib.sha256(content.encode()).hexdigest().encode())
            h.update(b"\n")
        else:
            h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode())
            h.update(b"\n")
    pyproject = THEME_DIR / "pyproject.toml"
    h.update(f"{pyproject.relative_to(REPO_ROOT)}\n".encode())
    h.update(hashlib.sha256(pyproject.read_bytes()).hexdigest().encode())
    h.update(b"\n")
    return h.hexdigest()


def get_current_version() -> str:
    text = INIT_FILE.read_text()
    match = re.search(r"^__version__ = ['\"]([^'\"]+)['\"]", text, re.MULTILINE)
    if not match:
        raise SystemExit("Could not find __version__ in __init__.py")
    return match.group(1)


def bump_version(version: str) -> str:
    major, minor, patch = version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


def git_add(*paths: Path) -> None:
    subprocess.check_call(["git", "add", *(str(p) for p in paths)])


def main() -> int:
    current_hash = compute_theme_hash()
    stored_hash = HASH_FILE.read_text().strip() if HASH_FILE.exists() else ""

    if current_hash == stored_hash:
        # No changes — just verify version file is in sync
        current_version = get_current_version()
        stored_version = VERSION_FILE.read_text().strip() if VERSION_FILE.exists() else ""
        if current_version != stored_version:
            VERSION_FILE.write_text(f"{current_version}\n")
            git_add(VERSION_FILE)
            print(f"sphinx_airflow_theme: synced LATEST_VERSION.txt to {current_version}")
        return 0

    # Hash changed — bump the patch version
    current_version = get_current_version()
    new_version = bump_version(current_version)
    print(f"sphinx_airflow_theme: files changed, bumping version {current_version} -> {new_version}")

    # Update __init__.py
    init_text = INIT_FILE.read_text()
    init_text = re.sub(r"^__version__ = .*", f"__version__ = '{new_version}'", init_text, flags=re.MULTILINE)
    init_text = re.sub(r"^__version_full__ = .*", "__version_full__ = __version__", init_text, flags=re.MULTILINE)
    INIT_FILE.write_text(init_text)

    # Recompute hash after version bump (version lines are excluded from hash)
    new_hash = compute_theme_hash()

    # Update stored hash and version
    HASH_FILE.write_text(f"{new_hash}\n")
    VERSION_FILE.write_text(f"{new_version}\n")

    # Stage the modified files
    git_add(INIT_FILE, HASH_FILE, VERSION_FILE)
    print("sphinx_airflow_theme: updated hash and version files")
    return 1


if __name__ == "__main__":
    sys.exit(main())
