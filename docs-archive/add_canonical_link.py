#!/usr/bin/env python3
from glob import glob
import logging
import sys
import os

log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    sub_dirs = get_sub_dirs()

    for sub_dir in sub_dirs:
        log.debug(f"Processing folder {sub_dir}")

        if os.path.isdir(sub_dir):
            package = os.path.basename(sub_dir)
            stable_version = get_stable_package_version(package)

            if not stable_version:
                continue

            if not os.path.isdir(f"./{package}/{stable_version}"):
                log.error(f"The package {package} does not have a directory for the stable version {stable_version}")

            doc_files = get_doc_files(package)
            for doc_file in doc_files:
                if is_doc_file_exists_in_stable(package, stable_version, doc_file):
                    add_canonical_link(package, doc_file)
                    pass
                else:
                    log.info(f"The doc file {doc_file} does not exist in stable version. Ignoring this file")


def get_sub_dirs():
    return glob("./*", recursive=False)


def get_stable_package_version(package: str):
    try:
        f = open(f"./{package}/stable.txt", "r")
        stable_version = f.read()
        f.close()
        log.debug(f"The stable version of {package} is {stable_version}")
        return stable_version
    except OSError:
        log.info(f"The package {package} does not have a stable.txt file. Ignoring this package")
        return None


def get_doc_files(package: str):
    # Ignore files under directories starting by "_"
    return [file for file in glob(f"./{package}/**/*.html", recursive=True) if "/_" not in file]


def is_doc_file_exists_in_stable(package: str, stable_version: str, doc_file: str):
    path = get_file_doc_path(doc_file)
    return os.path.isfile(f"./{package}/{stable_version}/{path}")


def get_file_doc_path(doc_file):
    # Given a file path, return the file path without the package name and version
    # Example: ./apache-airflow-providers-ssh/1.3.0/commits.html -> commits.html,
    return os.sep.join(os.path.normpath(doc_file).split(os.sep)[2:])


def add_canonical_link(package: str, doc_file: str):
    doc_file_content = get_file_content(doc_file)
    if 'rel="canonical"' in doc_file_content:
        log.warning(f"The file {doc_file} contains already a canonical link")
    else:
        doc_file_content = doc_file_content.replace(
            "</head>",
            f"<link rel=\"canonical\" href=\"https://airflow.apache.org/docs/{package}/stable/{get_file_doc_path(doc_file)}\" />\n</head>",
        )
        put_file_content(doc_file, doc_file_content)
        log.debug(f"Canonical link added to the file {doc_file}")


def get_file_content(file: str):
    try:
        f = open(file, "r")
        content = f.read()
        f.close()
        return content
    except OSError:
        log.error(f"Failed to open the file {file}")
        return None


def put_file_content(file: str, content: str):
    try:
        f = open(file, "w")
        f.write(content)
        f.close()
    except OSError:
        log.error(f"Failed to write file {file}")


main()
