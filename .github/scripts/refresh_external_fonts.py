#!/usr/bin/env python
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
# PEP 723 compliant inline script metadata
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
Refresh the self-hosted web fonts in landing-pages/site/static/external.

The site must not load fonts from fonts.googleapis.com at runtime (privacy), so
the Google Fonts CSS and font files are vendored. Google serves every font as a
set of per-script subsets (latin, latin-ext, cyrillic, ...), each a different
file selected by the browser through ``unicode-range``. Each subset is saved to
its own file here: storing them all under a single name keeps only the last
subset downloaded and silently drops e.g. the Latin glyphs.

Usage: uv run .github/scripts/refresh_external_fonts.py
"""

from __future__ import annotations

import http.client
import re
import time
import urllib.request
from pathlib import Path

EXTERNAL_DIR = Path(__file__).resolve().parents[2] / "landing-pages" / "site" / "static" / "external"
CSS_DIR = EXTERNAL_DIR / "css"
FONTS_DIR = EXTERNAL_DIR / "fonts"

# CSS file name (without .css) -> Google Fonts css2 "family" query.
FAMILIES = {
    "OpenSans": "Open+Sans:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700",
    "Roboto": "Roboto:ital,wght@0,400;0,500;0,700;1,400",
    "RobotoMono": "Roboto+Mono:wght@400;700",
    "Rubik": "Rubik:wght@500",
}

# Single-file names used before the fonts were split per subset. Browsers may keep
# serving cached copies of the old CSS, which still point at these names, so keep
# them as copies of the Latin subset (enough for every Latin-script page) until
# those caches have expired. Safe to drop after the 2027-03 site release.
LEGACY_ALIASES = {
    "OpenSans-italic.woff2": "OpenSans-italic-latin.woff2",
    "OpenSans-normal.woff2": "OpenSans-normal-latin.woff2",
    "Roboto-italic.woff2": "Roboto-italic-latin.woff2",
    "Roboto-normal.woff2": "Roboto-normal-latin.woff2",
    "RobotoMono-normal.woff2": "RobotoMono-normal-latin.woff2",
    "Rubik-normal.woff2": "Rubik-normal-latin.woff2",
}

# Google only returns woff2 (and unicode-range subsets) to modern browsers.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

BLOCK_RE = re.compile(r"/\* (?P<subset>[\w-]+) \*/\s*(?P<rule>@font-face \{.*?\})", re.S)
URL_RE = re.compile(r"url\((?P<url>https://fonts\.gstatic\.com/[^)]+)\)")
STYLE_RE = re.compile(r"font-style: (\w+);")


def fetch(url: str, attempts: int = 5) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except (OSError, http.client.HTTPException) as error:
            if attempt == attempts:
                raise
            print(f"Retrying {url} after {error!r}")
            time.sleep(attempt)
    raise AssertionError("unreachable")


def refresh_family(name: str, query: str) -> set[str]:
    css = fetch(f"https://fonts.googleapis.com/css2?family={query}&display=swap").decode()
    # Variable fonts serve all weights of a style/subset from one URL; download it once.
    local_names: dict[str, str] = {}
    out_blocks = []
    for block in BLOCK_RE.finditer(css):
        subset, rule = block["subset"], block["rule"]
        url = URL_RE.search(rule)["url"]
        if url not in local_names:
            style = STYLE_RE.search(rule)[1]
            file_name = f"{name}-{style}-{subset}.woff2"
            if file_name in local_names.values():
                raise SystemExit(f"{name}: two different files for {style}/{subset}; extend the naming scheme")
            (FONTS_DIR / file_name).write_bytes(fetch(url))
            local_names[url] = file_name
        out_blocks.append(f"/* {subset} */\n" + rule.replace(url, f"/external/fonts/{local_names[url]}"))
    if not out_blocks:
        raise SystemExit(f"{name}: no @font-face rules found in the Google Fonts response")
    (CSS_DIR / f"{name}.css").write_text("\n".join(out_blocks) + "\n")
    print(f"{name}: {len(out_blocks)} @font-face rules, {len(local_names)} font files")
    return set(local_names.values())


def main() -> None:
    written: set[str] = set()
    for name, query in FAMILIES.items():
        written |= refresh_family(name, query)
    for legacy, current in LEGACY_ALIASES.items():
        (FONTS_DIR / legacy).write_bytes((FONTS_DIR / current).read_bytes())
        written.add(legacy)
    for stale in sorted(FONTS_DIR.glob("*.woff2")):
        if stale.name not in written:
            print(f"Removing unused {stale.name}")
            stale.unlink()


if __name__ == "__main__":
    main()
