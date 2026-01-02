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
#
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "rich>=14.0.0",
# ]
# ///

import shutil
import argparse
from pathlib import Path

from rich.console import Console

console = Console(width=200, color_system="standard")

CSS_TO_ADD = """
  body {
      position: relative; /* Ensures the pseudo-element is positioned relative to the body */
      z-index: 0; /* Keeps the content above the pseudo-element */
  }

  body::before {
      content: "";
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: url(URL_PREFIX/staging.png) repeat center center fixed; /* Sets the background image */
      opacity: 0.2; /* Makes the watermark semi-transparent */
      pointer-events: none; /* Ensures the watermark doesn't interfere with user interactions */
      z-index: -1; /* Places the pseudo-element behind all other elements */
  }

  /* Dark mode support - increases watermark visibility */
  [data-theme="dark"] body::before,
  [data-bs-theme="dark"] body::before,
  .dark body::before,
  .dark-mode body::before {
      opacity: 0.4; /* Higher opacity for dark mode visibility */
      filter: invert(1) brightness(2); /* Inverts colors for dark background */
  }

  @media (prefers-color-scheme: dark) {
      body::before {
          opacity: 0.4;
          filter: invert(1) brightness(2);
      }
  }
"""


IMAGE_FILE=Path(__file__).parent / "images" / "staging.png"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add watermark")
    parser.add_argument("--folder", required=True, help="Folder to look for css files for")
    parser.add_argument("--pattern", required=True, help="Glob pattern to look for")
    parser.add_argument("--url-prefix", required=True, help="URL prefix to use for the image")
    parser.add_argument("--image-directory", required=True,
                        help="Image directory where image should be written-relative to folder path.")
    console.print("[bright_blue]Adding watermark to the site's CSS")
    args = parser.parse_args()

    folder_path = Path(args.folder)
    pattern = args.pattern
    url_prefix = args.url_prefix
    image_directory_path = Path(args.image_directory)

    content_to_add = CSS_TO_ADD.replace("URL_PREFIX", url_prefix)
    console.print(f"[bright_blue]Looking for css files following '{pattern}' pattern[/] in {folder_path}")
    files = folder_path.rglob(pattern)
    if not files:
        console.print(f"[red]No files found with pattern {pattern} in {folder_path}")
    else:
        for file in files:
            content = file.read_text()
            if not "watermark semi-transparent" in content:
                console.print(f"[yellow]Adding watermark to:[/] {file}")
                content = content + content_to_add
                file.write_text(content)
    target_image_location = folder_path / image_directory_path
    console.print(f"[yellow]Creating staging image at :[/]:{target_image_location}/staging.png")
    target_image_location.mkdir(parents=True, exist_ok=True)
    shutil.copy(IMAGE_FILE, target_image_location / "staging.png")
