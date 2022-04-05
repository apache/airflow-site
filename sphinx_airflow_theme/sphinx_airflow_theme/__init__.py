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

from os import path
from sphinx.application import Sphinx

__version__ = '0.0.7'
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


def setup_my_func(app, config):
    # We can't set this in the theme.conf, cos we want it to be a non-string type
    config.html_theme_options.setdefault('navbar_links', [{'href': '/index.html', 'text': 'Documentation'}])


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app: Sphinx):
    app.add_html_theme('sphinx_airflow_theme', path.abspath(path.dirname(__file__)))
    app.add_css_file('_gen/css/main-custom.min.css')
    app.connect("config-inited", setup_my_func)
    return {"version": "__version__", "parallel_read_safe": True, "parallel_write_safe": True}
