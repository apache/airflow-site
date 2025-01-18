#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MIT License
# 
# Copyright (c) 2025 Shashi Kumar
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import sys
import subprocess
import time
from pathlib import Path


def log(message):
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}:INFO: {message}")


def usage():
    print("""
    usage: <script> <command> [<args>]
    
    Available commands:
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
    original_directory = os.getcwd()
    os.chdir(working_directory)
    subprocess.run(args, check=True)
    os.chdir(original_directory)


def ensure_node_module_exists():
    log("Checking if node module exists")
    if not Path(MY_DIR, "landing-pages", "node_modules").exists():
        log("Missing node dependencies. Start installation.")
        run_command(MY_DIR + "/landing-pages", "yarn", "install")
        log("Dependencies installed.")


def ensure_that_website_is_build():
    log(f"Check if {MY_DIR}/landing-pages/dist/index.html exists")
    if not Path(MY_DIR, "landing-pages", "dist", "index.html").exists():
        log("The website is not built. Start building.")
        run_command(MY_DIR + "/landing-pages", "yarn", "run", "build")
        log("The website built.")


def relativepath(source, target):
    common_part = source
    result = ""

    while not target.startswith(common_part):
        common_part = os.path.dirname(common_part)
        result = "../" + result if result else ".."

    forward_part = target[len(common_part):]
    if common_part == "/":
        result = f"{result}/"

    if result and forward_part:
        result += forward_part
    elif forward_part:
        result = forward_part.lstrip("/")
    return result


def run_lint(script_working_directory, command, *args):
    mapped_paths = []
    for item in args:
        abs_path = os.path.abspath(item)
        mapped_paths.append(str(Path(MY_DIR, relativepath(os.getcwd(), abs_path))))
    run_command(script_working_directory, command, *mapped_paths)


def prepare_packages_metadata():
    log("Preparing packages-metadata.json")
    subprocess.run([f"{MY_DIR}/dump-docs-packages-metadata.py"], check=True, stdout=open(f"{MY_DIR}/landing-pages/site/static/_gen/packages-metadata.json", 'w'))


def build_landing_pages():
    log("Building landing pages")
    run_command(MY_DIR + "/landing-pages", "yarn", "run", "index")
    prepare_packages_metadata()
    run_command(MY_DIR + "/landing-pages", "yarn", "run", "build")


def create_redirect(output_file, target_location):
    log(f"Creating redirect: {output_file} => {target_location}")
    with open(output_file, "w") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
   <head><meta http-equiv="refresh" content="1; url={target_location}" /></head>
   <body></body>
</html>
""")


def verbose_copy(source, target):
    log(f"Copying '{source}' to '{target}'")
    os.makedirs(target, exist_ok=True)
    subprocess.run(["cp", "-R", source, target], check=True)


def assert_file_exists(file_path):
    if not os.path.isfile(file_path):
        print(f"Missing file: {file_path}")
        sys.exit(1)


def build_site():
    log("Building full site")

    if not Path(MY_DIR, "landing-pages", "dist", "index.html").exists():
        build_landing_pages()

    os.makedirs(Path(MY_DIR, "dist"), exist_ok=True)
    for item in Path(MY_DIR, "dist").iterdir():
        if item.exists():
            verbose_copy(str(item), str(Path(MY_DIR, "dist", item.name)))
    for pkg_path in Path(MY_DIR, "docs-archive").iterdir():
        if pkg_path.is_dir():
            package_name = pkg_path.name
            if (pkg_path / "stable.txt").exists():
                stable_version = open(pkg_path / "stable.txt").read().strip()
                verbose_copy(str(pkg_path / stable_version), f"dist/docs/{package_name}/stable")
                create_redirect(f"dist/docs/{package_name}/index.html", f"/docs/{package_name}/stable/index.html")
            else:
                verbose_copy(str(pkg_path), f"dist/docs/{package_name}/")

    prepare_packages_metadata()
    assert_file_exists(f"{MY_DIR}/dist/docs/index.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/index.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/1.10.7/tutorial.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/stable/tutorial.html")
    assert_file_exists(f"{MY_DIR}/dist/_gen/packages-metadata.json")


def prepare_theme():
    log("Preparing theme files")
    site_dist = Path(MY_DIR, "landing-pages", "dist")
    theme_gen = Path(MY_DIR, "sphinx_airflow_theme", "sphinx_airflow_theme", "static", "_gen")
    os.makedirs(theme_gen / "css", exist_ok=True)
    os.makedirs(theme_gen / "js", exist_ok=True)
    subprocess.run(["cp", str(site_dist / "docs.*.js"), str(theme_gen / "js/docs.js")], check=True)
    subprocess.run(["cp", str(site_dist / "scss/main.min.*.css"), str(theme_gen / "css/main.min.css")], check=True)
    subprocess.run(["cp", str(site_dist / "scss/main-custom.min.*.css"), str(theme_gen / "css/main-custom.min.css")], check=True)
    log("Successfully copied required files")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("You must provide at least one command.\n")
        usage()
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    MY_DIR = os.path.dirname(os.path.abspath(__file__))

    if cmd == "install-node-deps":
        subprocess.run(["npm", "install", "--global", "yarn"], check=True)
        run_command(MY_DIR + "/landing-pages", "yarn", "install")
    elif cmd == "preview-landing-pages":
        ensure_node_module_exists()
        run_command(MY_DIR + "/landing-pages", "yarn", "run", "index")
        prepare_packages_metadata()
        run_command(MY_DIR + "/landing-pages", "yarn", "run", "preview")
    elif cmd == "build-landing-pages":
        ensure_node_module_exists()
        build_landing_pages()
    elif cmd == "build-site":
        ensure_node_module_exists()
        build_site()
    elif cmd == "check-site-links":
        ensure_node_module_exists()
        ensure_that_website_is_build()
        run_command(MY_DIR + "/landing-pages", "./check-links.sh")
    elif cmd == "prepare-theme":
        ensure_that_website_is_build()
        prepare_theme()
    elif cmd == "lint-js":
        ensure_node_module_exists()
        if len(args) == 0:
            run_command(MY_DIR + "/landing-pages", "yarn", "run", "lint:js")
        else:
            run_lint(MY_DIR + "/landing-pages", "./node_modules/.bin/eslint", *args)
    elif cmd == "lint-css":
        ensure_node_module_exists()
        if len(args) == 0:
            run_command(MY_DIR + "/landing-pages", "yarn", "run", "lint:css")
        else:
            run_lint(MY_DIR + "/landing-pages", "./node_modules/.bin/stylelint", *args)
    else:
        usage()
        sys.exit(0)
