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
    run_command(f"{MY_DIR}/landing-pages/" ,"yarn", "run", "index")
    prepare_packages_metadata()
    run_command(f"{MY_DIR}/landing-pages/" ,"yarn" ,"run", "build")


def build_site():
    log("Building full site")
    if not os.path.isfile(f"{MY_DIR}/landing-pages/dist/index.html"):
        build_landing_pages()
        
    os.makedirs("dist",dirs_exist_ok=True)
    dist_path = 'dist/'

    for filename in os.listdir(dist_path):
        file_path = os.path.join(dist_path, filename)
        try:
           if os.path.isfile(file_path) or os.path.islink(file_path):
              os.remove(file_path)  # delete file or symbolic link
           elif os.path.isdir(file_path):
              shutil.rmtree(file_path)  # delete directory
        except Exception as e:
             print(f'Failed to delete {file_path}. Reason: {e}')
    verbose_copy("landing-pages/dist/.","dist/")
    dirs = [d for d in os.listdir("docs-archive") if os.path.isdir(os.path.join("docs-archive", d))]
    for pkg_path in dirs:
        if not os.path.isdir(pkg_path):
             continue
        path = f"{pkg_path}"
        package_name = os.path.basename(path)
        
        if os.isfile(f"{pkg_path}/stable.txt"):
           os.makedirs(f"docs-archive/{package_name}",exist_parent=True)
           dirs2 = [d for d in os.listdir(f"docs-archive/{package_name}") if os.path.isdir(os.path.join(f"docs-archive/{package_name}", d))]
           for ver_path in dirs2:
               path = f"{ver_path}"
               version=os.path.basename(path)
               verbose_copy(f"docs-archive/{package_name}/{version}/.","dist/docs/${package_name}/${version}")
               create_redirect(f"dist/docs/{package_name}/index.html",f"/docs/{package_name}/stable/index.html")
        else:
            verbose_copy(f"docs-archive/{package_name}/.",f"dist/docs/{package_name}/")
    log("Preparing packages-metadata.json")
    command=f"{MY_DIR}/dump-docs-packages-metadata.py"
    with open(f"{MY_DIR}/dist/_gen/packages-metadata.json", "w") as file:
        subprocess.run(command, stdout=file, stderr=subprocess.STDOUT)
    assert_file_exists(f"{MY_DIR}/dist/docs/index.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/index.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/1.10.7/tutorial.html")
    assert_file_exists(f"{MY_DIR}/dist/docs/apache-airflow/stable/tutorial.html")
    assert_file_exists(f"{MY_DIR}/dist/_gen/packages-metadata.json")
    
    
def ensure_node_module_exists():
    log("Checking if node module exists")
    if os.path.isdir(f"{MY_DIR}/landing-pages/node_modules/"):
        log("Missing node dependencies. Start installation.")
        run_command("./landing-pages/","yarn","install")
        log("Dependencies installed.")


def ensure_that_website_is_build():
    log("Check if ${MY_DIR}/landing-pages/dist/index.html file exists")
    if not os.path.isfile(f"{MY_DIR}/landing-pages/dist/index.html"):
        log("The website is not built. Start building.")
        run_command("${MY_DIR}/landing-pages/","yarn","run","build")
        log("The website built.")


def relativepath(source, target):
    # Get the absolute paths
    source = os.path.abspath(source)
    target = os.path.abspath(target)

    common_part = source  # For now, assume the entire source is common
    result = ""  # To store the relative path

    # Loop to find the common path
    while not target.startswith(common_part.rstrip(os.sep) + os.sep) and common_part != os.sep:
        common_part = os.path.dirname(common_part)
        # Add ".." to the result for each step up
        result = ".." if result == "" else os.path.join("..", result)

    # Special case for root ("/")
    if common_part == os.sep:
        result = os.path.join(result, os.sep)

    # Compute the non-common part (forward part)
    forward_part = target[len(common_part):]

    # Concatenate the result and forward part
    if result and forward_part:
        result = os.path.join(result, forward_part.lstrip(os.sep))
    elif forward_part:
        result = forward_part.lstrip(os.sep)

    return result



def run_command(*args):
    working_dir=args[0]
    log(f"Changing to {working_dir} and running: {args[1:]}")
    os.chdir(f"{working_dir}")
    subprocess.run(args[1:])

def run_lint(*args): 
    script_working_directory = args[0]
    command = args[1]
    entries = args[2:]
    mapped_paths = []

    flat_paths = []
    for e in entries:
        if isinstance(e, list):
            flat_paths.extend(e)
        else:
            flat_paths.append(e)

    for path in flat_paths:
        abs_path = os.path.realpath(f"{WORKING_DIR}/{path}")
        rel_path = os.path.relpath(abs_path, start=os.getcwd())
        mapped_path = f"{MY_DIR}/{rel_path}"
        mapped_paths.append(mapped_path)

    command_with_args = [command] + mapped_paths
    subprocess.run(command_with_args, cwd=script_working_directory, check=True)

def log(*message):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{time_stamp}:INFO: ",end = "")
    print(' '.join(message))


def verbose_copy(*args):
    source=args[0]
    target=args[1]
    log(f"Copying {source} to {target}")
    os.makedirs(f"{target}", exist_ok=True)
    shutil.copytree(src=source,dst=target,dirs_exist_ok=True)


def create_redirect(*args):
    output_file=args[0]
    target_location=args[1]
    log(f"Creating redirect: {output_file} => {target_location}")

    with open(f'{output_file}', 'w') as file:
        file.write("""<!DOCTYPE html>
<html>
   <head><meta http-equiv="refresh" content="1; url=${target_location}" /></head>
   <body></body>
</html>""")


def assert_file_exists(*args):
    if not os.path.isfile(f"{args[0]}"):
        print(f"Missing file: {args[0]}")
        sys.exit()



def prepare_theme():
    log("Preparing theme files")
    SITE_DIST=f"{MY_DIR}/landing-pages/dist"
    THEME_GEN=f"{MY_DIR}/sphinx_airflow_theme/sphinx_airflow_theme/static/_gen"
    os.makedirs(f"{THEME_GEN}/css",exist_ok=True)
    os.makedirs(f"{THEME_GEN}/js",exist_ok=True)
    shutil.copytree(src=f"{SITE_DIST}/docs.*.js",dst=f"{THEME_GEN}/js/docs.js",exist_ok=True)
    shutil.copytree(src=f"{SITE_DIST}/scss/main.min.*.css",dst=f"{THEME_GEN}/css/main.min.css",exist_ok=True)
    shutil.copytree(src=f"{SITE_DIST}/scss/main-custom.min.*.css",dst=f"{THEME_GEN}/css/main-custom.min.css",exist_ok=True)
    print("Successful copied required files")


    
def prepare_packages_metadata():
    log("Preparing packages-metadata.json")
    command=f"{MY_DIR}/dump-docs-packages-metadata.py"
    with open(f"{MY_DIR}/landing-pages/site/static/_gen/packages-metadata.json", "w") as file:
        subprocess.run(command, stdout=file, stderr=subprocess.STDOUT)


if _name_ == "_main_":
   
   parser = argparse.ArgumentParser()
   parser.add_argument("arg1")
   parser.add_argument("arg2", nargs="*", help="Optional argument for files", default=None)
   args = parser.parse_args()
   
   if args.arg1 == "help" :
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

The lint-css and lint-js commands accept paths in arguments. If no path is given,
the script will be executed for all supported files.
""")
   if args.arg2:
     run_lint(f"{MY_DIR}/landing-pages/", "./node_modules/.bin/eslint", *args.arg2)
   elif args.arg1 == "install-node-deps" :
       subprocess.run(['npm','install','--global','yarn'])
       run_command(f"{MY_DIR}/landing-pages/","yarn","install")
   elif args.arg1 == "preview-landing-pages":
       ensure_node_module_exists()
       run_command(f"{MY_DIR}/landing-pages/","yarn","run","index")
       prepare_packages_metadata()
       run_command(f"{MY_DIR}/landing-pages" ,"yarn" ,"run", "preview")
   elif args.arg1 == "build-landing-pages" :
       ensure_node_module_exists()
       build_landing_pages()
       
   elif args.arg1 == "build-site" :
       ensure_node_module_exists()
       build_site()
       
   elif args.arg1 == "check-site-links" :
       ensure_node_module_exists()
       ensure_that_website_is_build()
       run_command("${MY_DIR}/landing-pages/","./check-links.sh")
   
   elif args.arg1 == "prepare-theme" :
       ensure_that_website_is_build()
       prepare_theme()
   
   
   elif args.arg1 == "lint-js" :
       ensure_node_module_exists()
       if len(sys.argv) == 1:  # No positional arguments
         landing_pages_path = os.path.join(MY_DIR, "landing-pages")
         subprocess.run(["yarn", "run", "lint:js"], cwd=landing_pages_path)
       else :
         run_lint(f"{MY_DIR}/landing-pages/","./node_modules/.bin/eslint",*sys.argv[2:])
         
       
         
   elif args.arg1 == "lint-css" :
       ensure_node_module_exists()
       if len(sys.argv) == 2:  # Only the script name and 'lint-css' present
        subprocess.run(["yarn", "run", "lint:css"], cwd=landing_pages_path)
       else :
         run_lint(f"{MY_DIR}/landing-pages/","./node_modules/.bin/stylelint",*sys.argv[2:])
