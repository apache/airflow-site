#!/usr/bin/env python3

import argparse
from datetime import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Constants
MY_DIR = os.path.dirname(os.path.abspath(__file__))
WORKING_DIR = os.getcwd()


def build_landing_pages():
    log("Building landing pages")
    run_command(f"{MY_DIR}/landing-pages/", "yarn", "run", "index")
    prepare_packages_metadata()
    run_command(f"{MY_DIR}/landing-pages/", "yarn", "run", "build")


def build_site():
    log("Building full site")
    if not os.path.isfile(f"{MY_DIR}/landing-pages/dist/index.html"):
        build_landing_pages()

    dist_path = 'dist/'
    os.makedirs(dist_path, exist_ok=True)

    # Clean up old dist contents
    for filename in os.listdir(dist_path):
        file_path = os.path.join(dist_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    verbose_copy("landing-pages/dist/", "dist/")

    for package_name in os.listdir("docs-archive"):
        pkg_path = os.path.join("docs-archive", package_name)
        if not os.path.isdir(pkg_path):
            continue

        stable_file = os.path.join(pkg_path, "stable.txt")
        if os.path.isfile(stable_file):
            os.makedirs(f"docs-archive/{package_name}", exist_ok=True)
            for version in os.listdir(pkg_path):
                version_path = os.path.join(pkg_path, version)
                if os.path.isdir(version_path):
                    verbose_copy(version_path + "/", f"dist/docs/{package_name}/{version}")
                    create_redirect(f"dist/docs/{package_name}/index.html",
                                    f"/docs/{package_name}/stable/index.html")
        else:
            verbose_copy(pkg_path + "/", f"dist/docs/{package_name}/")

    log("Preparing packages-metadata.json")
    command = [sys.executable, f"{MY_DIR}/dump-docs-packages-metadata.py"]
    os.makedirs(f"{MY_DIR}/dist/_gen", exist_ok=True)
    with open(f"{MY_DIR}/dist/_gen/packages-metadata.json", "w") as file:
        subprocess.run(command, stdout=file, stderr=subprocess.STDOUT)

    assert_file_exists(f"{MY_DIR}/dist/docs/index.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/index.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/1.10.7/tutorial.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/stable/tutorial.html")
    assert_file_exists(f"{MY_DIR}/dist/_gen/packages-metadata.json")


def ensure_node_module_exists():
    log("Checking if node_modules/ exists")
    if not os.path.isdir(f"{MY_DIR}/landing-pages/node_modules/"):
        log("Missing node dependencies. Start installation.")
        run_command(f"{MY_DIR}/landing-pages/", "yarn", "install")
        log("Dependencies installed.")


def ensure_that_website_is_build():
    log(f"Check if {MY_DIR}/landing-pages/dist/index.html file exists")
    if not os.path.isfile(f"{MY_DIR}/landing-pages/dist/index.html"):
        log("The website is not built. Start building.")
        run_command(f"{MY_DIR}/landing-pages/", "yarn", "run", "build")
        log("The website built.")


def relativepath(source, target):
    return os.path.relpath(os.path.abspath(target), os.path.abspath(source))


def run_command(*args):
    working_dir = args[0]
    log(f"Changing to {working_dir} and running: {args[1:]}")
    subprocess.run(args[1:], cwd=working_dir)


def run_lint(script_working_directory, command, *entries):
    flat_paths = []
    for e in entries:
        if isinstance(e, list):
            flat_paths.extend(e)
        else:
            flat_paths.append(e)

    mapped_paths = []
    for path in flat_paths:
        abs_path = os.path.realpath(os.path.join(WORKING_DIR, path))
        rel_path = os.path.relpath(abs_path, start=os.getcwd())
        mapped_path = os.path.join(MY_DIR, rel_path)
        mapped_paths.append(mapped_path)

    subprocess.run([command] + mapped_paths, cwd=script_working_directory, check=True)


def log(*message):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{time_stamp}:INFO: ", end="")
    print(' '.join(message))


def verbose_copy(source, target):
    log(f"Copying {source} to {target}")
    shutil.copytree(source, target, dirs_exist_ok=True)


def create_redirect(output_file, target_location):
    log(f"Creating redirect: {output_file} => {target_location}")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as file:
        file.write(f"""<!DOCTYPE html>
<html>
   <head><meta http-equiv="refresh" content="1; url={target_location}" /></head>
   <body></body>
</html>""")


def assert_file_exists(path):
    if not os.path.isfile(path):
        print(f"Missing file: {path}")
        sys.exit(1)


def prepare_theme():
    log("Preparing theme files")
    SITE_DIST = f"{MY_DIR}/landing-pages/dist"
    THEME_GEN = f"{MY_DIR}/sphinx_airflow_theme/sphinx_airflow_theme/static/_gen"
    os.makedirs(f"{THEME_GEN}/css", exist_ok=True)
    os.makedirs(f"{THEME_GEN}/js", exist_ok=True)

    shutil.copy(os.path.join(SITE_DIST, "docs.js"), f"{THEME_GEN}/js/docs.js")
    shutil.copy(os.path.join(SITE_DIST, "scss/main.min.css"), f"{THEME_GEN}/css/main.min.css")
    shutil.copy(os.path.join(SITE_DIST, "scss/main-custom.min.css"), f"{THEME_GEN}/css/main-custom.min.css")
    print("Successfully copied required files")


def prepare_packages_metadata():
    log("Preparing packages-metadata.json")

    commands = [
    "pip install venv",
    "python3 -m venv myenv",
    "source myenv/bin/activate && pip install semver"
     ]

    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

    # Ensure target directory exists
    os.makedirs(f"{MY_DIR}/landing-pages/site/static/_gen", exist_ok=True)

    # Run dump-docs-packages-metadata.py inside venv
    python_path = os.path.join(venv_path, "bin", "python")
    command = [python_path, f"{MY_DIR}/dump-docs-packages-metadata.py"]
    with open(f"{MY_DIR}/landing-pages/site/static/_gen/packages-metadata.json", "w") as file:
        subprocess.run(command, stdout=file, stderr=subprocess.STDOUT)

    log("packages-metadata.json generated successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1")
    parser.add_argument("arg2", nargs="*", help="Optional argument for files", default=[])
    args = parser.parse_args()

    if args.arg1 == "help":
        print("""usage: site.py <command> [<args>]

These are the site.py commands that can be used in various situations:

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
    elif args.arg1 == "install-node-deps":
        subprocess.run(['npm', 'install', '--global', 'yarn'])
        run_command(f"{MY_DIR}/landing-pages/", "yarn", "install")

    elif args.arg1 == "preview-landing-pages":
        ensure_node_module_exists()
        run_command(f"{MY_DIR}/landing-pages/", "yarn", "run", "index")
        prepare_packages_metadata()
        run_command(f"{MY_DIR}/landing-pages", "yarn", "run", "preview")

    elif args.arg1 == "build-landing-pages":
        prepare_packages_metadata()
        ensure_node_module_exists()
        build_landing_pages()

    elif args.arg1 == "build-site":
        ensure_node_module_exists()
        build_site()

    elif args.arg1 == "check-site-links":
        ensure_node_module_exists()
        ensure_that_website_is_build()
        run_command(f"{MY_DIR}/landing-pages/", "./check-links.sh")

    elif args.arg1 == "prepare-theme":
        ensure_that_website_is_build()
        prepare_theme()

    elif args.arg1 == "lint-js":
        ensure_node_module_exists()
        if not args.arg2:
            subprocess.run(["yarn", "run", "lint:js"], cwd=os.path.join(MY_DIR, "landing-pages"))
        else:
            run_lint(f"{MY_DIR}/landing-pages/", "./node_modules/.bin/eslint", *args.arg2)

    elif args.arg1 == "lint-css":
        ensure_node_module_exists()
        if not args.arg2:
            subprocess.run(["yarn", "run", "lint:css"], cwd=os.path.join(MY_DIR, "landing-pages"))
        else:
            run_lint(f"{MY_DIR}/landing-pages/", "./node_modules/.bin/stylelint", *args.arg2)
