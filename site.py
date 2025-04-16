#!/usr/bin/env python3


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

import argparse
import datetime
import os
import subprocess
import sys
from pathlib import Path
import shutil

def log(message):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{now} INFO: {message}", file=sys.stderr)

def usage():
    print("""usage: site.py <command> [<args>]

Commands:
    build-site            Prepare dist/ directory with landing pages and docs.
    preview-landing-pages Start the web server with preview of the landing pages.
    build-landing-pages   Build the landing pages.
    prepare-theme         Copy required CSS/JS files from landing pages into the docs theme.
    install-node-deps     Download all the Node dependencies.
    check-site-links      Check to make sure that links are correct in the website.
    lint-css              Lint CSS files.
    lint-js               Lint Javascript files.
    help                  Display usage.
""")

def run_command(working_directory, *args):
    log(f"Changing to {working_directory} and running: {' '.join(args)}")
    subprocess.run(args, cwd=working_directory, check=True)

def assert_file_exists(filepath):
    if not Path(filepath).is_file():
        log(f"Missing file: {filepath}")
        sys.exit(1)

def ensure_node_module_exists():
    node_modules_path = Path(MY_DIR) / "landing-pages" / "node_modules"
    if not node_modules_path.exists():
        log("Missing node dependencies. Start installation.")
        run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "install")
        log("Dependencies installed.")

def prepare_packages_metadata():
    log("Preparing packages-metadata.json")
    output_path = Path(MY_DIR) / "landing-pages/site/static/_gen/packages-metadata.json"
    with open(output_path, "w") as f:
        subprocess.run([str(Path(MY_DIR) / "dump-docs-packages-metadata.py")], stdout=f)

def build_landing_pages():
    log("Building landing pages")
    run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "run", "index")
    prepare_packages_metadata()
    run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "run", "build")

def build_site():
    log("Building full site")
    index_file = Path(MY_DIR) / "landing-pages/dist/index.html"
    if not index_file.is_file():
        build_landing_pages()

    dist_dir = Path(MY_DIR) / "dist"
    dist_dir.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(dist_dir)
    shutil.copytree(Path(MY_DIR) / "landing-pages/dist", dist_dir, dirs_exist_ok=True)

    docs_archive = Path(MY_DIR) / "docs-archive"
    for pkg_path in docs_archive.iterdir():
        if not pkg_path.is_dir():
            continue

        package_name = pkg_path.name
        stable_txt = pkg_path / "stable.txt"
        if stable_txt.is_file():
            for ver_path in pkg_path.iterdir():
                if ver_path.is_dir():
                    target = dist_dir / "docs" / package_name / ver_path.name
                    shutil.copytree(ver_path, target, dirs_exist_ok=True)
            stable_version = stable_txt.read_text().strip()
            stable_path = pkg_path / stable_version
            stable_target = dist_dir / "docs" / package_name / "stable"
            shutil.copytree(stable_path, stable_target, dirs_exist_ok=True)
            create_redirect(dist_dir / "docs" / package_name / "index.html", f"/docs/{package_name}/stable/index.html")
        else:
            shutil.copytree(pkg_path, dist_dir / "docs" / package_name, dirs_exist_ok=True)

    prepare_packages_metadata()

    assert_file_exists(dist_dir / "docs/index.html")
    assert_file_exists(dist_dir / "docs/apache-airflow/index.html")
    assert_file_exists(dist_dir / "docs/apache-airflow/1.10.7/tutorial.html")
    assert_file_exists(dist_dir / "docs/apache-airflow/stable/tutorial.html")
    assert_file_exists(dist_dir / "_gen/packages-metadata.json")

def create_redirect(output_file, target_location):
    log(f"Creating redirect: {output_file} => {target_location}")
    with open(output_file, "w") as f:
        f.write(f"""<!DOCTYPE html>
<html>
   <head><meta http-equiv=\"refresh\" content=\"1; url={target_location}\" /></head>
   <body></body>
</html>
""")

def prepare_theme():
    log("Preparing theme files")
    site_dist = Path(MY_DIR) / "landing-pages/dist"
    theme_gen = Path(MY_DIR) / "sphinx_airflow_theme/sphinx_airflow_theme/static/_gen"
    (theme_gen / "css").mkdir(parents=True, exist_ok=True)
    (theme_gen / "js").mkdir(parents=True, exist_ok=True)

    shutil.copy(next(site_dist.glob("docs.*.js")), theme_gen / "js/docs.js")
    shutil.copy(next(site_dist.glob("scss/main.min.*.css")), theme_gen / "css/main.min.css")
    shutil.copy(next(site_dist.glob("scss/main-custom.min.*.css")), theme_gen / "css/main-custom.min.css")
    print("Successfully copied required files")

if __name__ == '__main__':
    MY_DIR = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd == "help":
        usage()
    elif cmd == "install-node-deps":
        subprocess.run(["npm", "install", "--global", "yarn"])
        run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "install")
    elif cmd == "preview-landing-pages":
        ensure_node_module_exists()
        run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "run", "index")
        prepare_packages_metadata()
        run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "run", "preview")
    elif cmd == "build-landing-pages":
        ensure_node_module_exists()
        build_landing_pages()
    elif cmd == "build-site":
        ensure_node_module_exists()
        build_site()
    elif cmd == "check-site-links":
        ensure_node_module_exists()
        run_command(str(Path(MY_DIR) / "landing-pages"), "./check-links.sh")
    elif cmd == "prepare-theme":
        prepare_theme()
    elif cmd == "lint-css":
        ensure_node_module_exists()
        if not args:
            # No additional paths passed, run full lint
            run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "run", "lint:css")
        else:
            # Custom path linting using stylelint
            lint_args = args
            stylelint_bin = str(Path(MY_DIR) / "landing-pages" / "node_modules" / ".bin" / "stylelint")
            run_command(str(Path(MY_DIR) / "landing-pages"), stylelint_bin, *lint_args)
    elif cmd == "lint-js":
        ensure_node_module_exists()
        if not args:
            # No additional lint target, run full JS lint
            run_command(str(Path(MY_DIR) / "landing-pages"), "yarn", "run", "lint:js")
        else:
            # Custom JS linting using eslint
            lint_args = args
            eslint_bin = str(Path(MY_DIR) / "landing-pages" / "node_modules" / ".bin" / "eslint")
            run_command(str(Path(MY_DIR) / "landing-pages"), eslint_bin, *lint_args)
    else:
        usage()
        sys.exit(1)
