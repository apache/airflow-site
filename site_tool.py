import argparse
import contextlib
from pathlib import Path
import os
import glob
import re
import sys
import shutil
import subprocess
from typing import Union, List, Optional, Mapping
from dump_docs_packages_metadata import dump_docs_package_metadata
# from bs4 import BeautifulSoup
IMAGE_NAME="airflow-site"
CONTAINER_NAME="airflow-site-c"
RunCommandResult = Union[subprocess.CompletedProcess, subprocess.CalledProcessError]


def run_command(cmd: List[str],
    env: Optional[Mapping[str, str]] = None,
    cwd: Optional[Path] = None,
    input: Optional[str] = None,
    check: bool = True,
     **kwargs,
)-> RunCommandResult:
    workdir: str = str(cwd) if cwd else os.getcwd()
    try:
        cmd_env = os.environ.copy()
        cmd_env.setdefault("HOME", str(Path.home()))
        if env:
            cmd_env.update(env)
        return subprocess.run(cmd, input=input, check=check, env=cmd_env, cwd=workdir, **kwargs)
    except subprocess.CalledProcessError as ex:
        if ex.stdout:
            print(ex.stdout)
        if ex.stderr:
            print(ex.stderr)
        return ex

def prepare_package_metadata(file_path):
    print("Preparing packages-metadata.json")
    dump_docs_package_metadata(file_path)

def sanity_checks_files(file_list):
    for file_to_check in file_list:
        if not file_to_check.exists():
            print("Missing file:", str(file_to_check))
            sys.exit(1)

def build_site():
    print("Building full site")
    landing_page = Path("landing-pages/dist/index.html")
    if not landing_page.exists():
        build_landing_page()
    DIST = Path.cwd()/ "dist"
    # DIST.mkdir(parents=True, exist_ok=True)
    # files = DIST.glob('**/*')
    # for file_to_delete in files:
    shutil.rmtree(str(DIST))
    shutil.copytree("landing-pages/dist/.","dist/")
    for package_name in next(os.walk('docs-archive'))[1]:
        stable_path = Path('docs-archive')/ package_name/ 'stable.txt'
        if stable_path.exists():
            for version in next(os.walk('docs-archive/'+package_name))[1]:
                shutil.copytree(str(Path("docs-archive")/package_name/version/"."), str(Path("dist")/"docs"/package_name/version))
            stable_version = stable_path.read_text()
            shutil.copytree(str(Path("docs-archive")/package_name/stable_version/"."), str(Path("dist")/"docs"/package_name/"stable"))
        else:
            shutil.copytree("docs-archive/"+package_name+"/.", "dist/docs/"+package_name)
    prepare_package_metadata(Path.cwd()/"dist"/"_gen"/"packages-metadata.json")
    files_to_check = [
        Path.cwd()/Path("dist/docs/index.html"),
        Path.cwd()/Path("dist/docs/apache-airflow/1.10.7/tutorial.html"),
        Path.cwd()/Path("dist/docs/apache-airflow/stable/tutorial.html"),
        Path.cwd()/Path("dist/_gen/packages-metadata.json"),
    ]
    sanity_checks_files(files_to_check)

def run_build_site(args):
    """
    Prepare dist directory with landing pages and documentation.
    """
    ensure_node_module_exists()
    build_site()

def ensure_node_module_exists():
    print("Checking if node module exists")
    node_dependency = Path(Path.cwd()/'landing-pages'/'node_modules')
    if not node_dependency.exists():
        print("Missing node dependencies. Start installation.")
        run_command(['yarn', 'install'], cwd=Path.cwd()/'landing-pages')
        print("Dependencies installed.")

def ensure_that_website_is_build():
    print("Check if landing-pages/dist/index.html file exists")
    landing_page = Path.cwd()/Path("landing-pages/dist/index.html")
    if not landing_page.exists():
        print("The website is not built. Start building.")
        run_command(['npm', 'run', 'build'], cwd=Path.cwd()/"landing-pages")
        print("The website is built.")

def run_install_node_deps(args):
    """
    Download all the Node dependencies.
    """
    run_command(['yarn', 'install'], cwd=Path.cwd()/"landing-pages")

def preview_landing_pages():
    run_command(['yarn', 'run', 'index'], cwd=Path.cwd()/"landing-pages")
    prepare_package_metadata(Path.cwd()/"landing-pages/site/static/_gen/packages-metadata.json")
    run_command(['yarn', 'run', 'preview'], cwd=Path.cwd()/"landing-pages")

def run_preview_landing_pages(args):
    """Starts the web server with preview of the website."""
    ensure_node_module_exists()
    preview_landing_pages()

def build_landing_page():
    print("Building landing page")
    run_command(['yarn', 'run', 'index'], cwd=Path.cwd()/"landing-pages")
    prepare_package_metadata(Path.cwd()/"landing-pages/site/static/_gen/packages-metadata.json")
    run_command(['yarn', 'run', 'build'], cwd=Path.cwd()/"landing-pages")

def run_build_landing_pages(args):
    """Build the landing pages."""
    ensure_node_module_exists()
    build_landing_page()

@contextlib.contextmanager
def working_directory(source_path: Path):
    prev_cwd = Path.cwd()
    os.chdir(source_path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)

# def extract_links(file_path):
#     links = []
#     with open(file_path) as file_content:
#         urls = file_content.read()
#         #  grep "^https\?://"
#         links = re.findall(r'(https?://[^\s]+)', urls)
#         # links = re.findall( "^https\?://", urls)
#     # print(links)
#     return links

# @working_directory(Path.cwd()/"landing-pages")
# def run_check_site_links(args):
#     dist = Path.cwd()/"dist"
#     index_page = dist/"index.html"
#     if not index_page.exists():
#         print("You should build website first.")
#         sys.exit(1)
#     html_files = dist.glob('**/*.html')
#     count = 0
#     external_links = set()
#     for html_file in html_files:
#         # print(html_file)
#         count += 1
#         external_links.update(extract_links(html_file))
#     with open("test.txt","w") as test:
#         for item in external_links:
#             test.write("%s\n" % item)
#     print(external_links, len(external_links))

def run_check_site_links(args):
    """Check to make sure that links are correct in the website."""
    ensure_node_module_exists()
    ensure_that_website_is_build()
    run_command(['./check-links.sh'], cwd=Path.cwd()/"landing-pages")

def copy_file_with_pattern(src_file_pattern, destination_file):
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    for file in glob.glob(src_file_pattern):
        shutil.copy(file, destination_file)

def prepare_theme():
    print("Preparing theme files")
    SITE_DIST = Path.cwd()/ "landing-pages/dist"
    THEME_GEN = Path.cwd()/ "sphinx_airflow_theme/sphinx_airflow_theme/static/_gen"
    SITE_DIST.mkdir(parents=True, exist_ok=True)
    THEME_GEN.mkdir(parents=True, exist_ok=True)
    copy_file_with_pattern(str(SITE_DIST)+"/docs.*.js", str(THEME_GEN)+"/js/docs.js")
    copy_file_with_pattern(str(SITE_DIST)+"/scss/main.min.*.css", str(THEME_GEN)+"/css/main.min.css")
    copy_file_with_pattern(str(SITE_DIST)+"/scss/main-custom.min.*.css", str(THEME_GEN)+"/css/main-custom.min.css")
    print("Successful copied required files")

def run_prepare_theme(args):
    """Copy required CSS/JS files from landing pages into the docs theme."""
    ensure_that_website_is_build()
    prepare_theme()

def run_lint_css(args):
    """Lint CSS files."""
    ensure_node_module_exists()
    if args.filename == ['-']:
       run_command(['yarn', 'run', 'lint:css'], cwd=Path.cwd()/"landing-pages")
    else:
        cmd_to_run = ['./node_modules/.bin/eslint']
        for filepath in args.filename:
            filename = Path(filepath).resolve()
            cmd_to_run.append(str(filename))
        run_command(cmd_to_run, cwd=Path.cwd()/"landing-pages", capture_output=True)


def run_lint_js(args):
    """Lint Javascript files."""
    ensure_node_module_exists()
    if args.filename == ['-']:
        run_command(['yarn', 'run', 'lint:js'], cwd=Path.cwd()/"landing-pages")
    else:
        cmd_to_run = ['./node_modules/.bin/eslint']
        for filepath in args.filename:
            filename = Path(filepath).resolve()
            cmd_to_run.append(str(filename))
        run_command(cmd_to_run, cwd=Path.cwd()/"landing-pages", capture_output=True)

def ger_parser():
    parser = argparse.ArgumentParser(
        description="Various commands used to build the airflow site", formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(help="sub-command help", metavar="COMMAND")
    subparsers.required = True

    parser_install_node_deps = subparsers.add_parser("install-node-deps", help=run_install_node_deps.__doc__)
    parser_install_node_deps.set_defaults(func=run_install_node_deps)

    parser_preview_landing_page = subparsers.add_parser("preview-landing-pages", help=run_preview_landing_pages.__doc__)
    parser_preview_landing_page.set_defaults(func=run_preview_landing_pages)

    parser_build_site = subparsers.add_parser("build-site", help=run_build_site.__doc__)
    parser_build_site.set_defaults(func=run_build_site)

    parser_build_landing_page = subparsers.add_parser("build-landing-pages", help=run_build_landing_pages.__doc__)
    parser_build_landing_page.set_defaults(func=run_build_landing_pages)

    parser_check_site_links = subparsers.add_parser("check-site-links",
    help=run_check_site_links.__doc__)
    parser_check_site_links.set_defaults(func=run_check_site_links)

    parser_prepare_theme = subparsers.add_parser("prepare-theme",
    help=run_prepare_theme.__doc__)
    parser_prepare_theme.set_defaults(func=run_prepare_theme)

    parser_lint_js = subparsers.add_parser("lint-js",help=run_lint_js.__doc__)
    parser_lint_js.set_defaults(func=run_lint_js)
    parser_lint_js.add_argument('filename', nargs='*', default=['-'])

    parser_lint_css = subparsers.add_parser("lint-css",help=run_lint_css.__doc__)
    parser_lint_css.set_defaults(func=run_lint_css)
    parser_lint_css.add_argument('filename', nargs='*', default=['-'])
    return parser


parser = ger_parser()

args = parser.parse_args()
args.func(args)
