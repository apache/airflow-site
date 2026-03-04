#!/bin/bash
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

set -e

echo "Generating missing favicons from Airflow pinwheel logo..."

SOURCE_SVG="site/static/images/airflow-icon.svg"
DEST_DIR="site/static/favicons"
TEMP_PNG="/tmp/airflow-logo-1024.png"

if [ ! -f "$SOURCE_SVG" ]; then
    echo "Error: Source SVG not found at $SOURCE_SVG"
    exit 1
fi

mkdir -p "$DEST_DIR"

echo "Converting SVG to high-resolution PNG with padding..."
# Render SVG at high resolution, then add ~10% padding on each side so the icon
# is not clipped in Chromium-based browsers or Google Search results (see #1432).
rsvg-convert -w 1024 -h 1024 "$SOURCE_SVG" -o "$TEMP_PNG"
PADDED_PNG="/tmp/airflow-logo-padded.png"
magick "$TEMP_PNG" -gravity center -background transparent -extent 1230x1230 "$PADDED_PNG"

echo "Generating ALL favicon files..."

# Helper: generate a padded square favicon PNG
generate_favicon() {
    local size=$1
    local output=$2
    magick "$PADDED_PNG" -resize "${size}x${size}" "$output"
}

# Generate standard favicon sizes
generate_favicon 16 "$DEST_DIR/favicon-16x16.png"
generate_favicon 32 "$DEST_DIR/favicon-32x32.png"
generate_favicon 96 "$DEST_DIR/favicon-96x96.png"
generate_favicon 256 "$DEST_DIR/favicon-256.png"
magick "$PADDED_PNG" -resize 1024x1024 "$DEST_DIR/favicon-1024.png"

# Generate favicon.ico with multiple sizes (16, 32, 48)
generate_favicon 16 /tmp/favicon-16.png
generate_favicon 32 /tmp/favicon-32.png
generate_favicon 48 /tmp/favicon-48.png
magick /tmp/favicon-16.png /tmp/favicon-32.png /tmp/favicon-48.png "$DEST_DIR/favicon.ico"

# Generate android-* files (without -icon- in name)
generate_favicon 36 "$DEST_DIR/android-36x36.png"
generate_favicon 48 "$DEST_DIR/android-48x48.png"
generate_favicon 72 "$DEST_DIR/android-72x72.png"
generate_favicon 96 "$DEST_DIR/android-96x96.png"
generate_favicon 144 "$DEST_DIR/android-144x144.png"
generate_favicon 192 "$DEST_DIR/android-192x192.png"

# Generate android-icon-* files (with -icon- in name)
generate_favicon 36 "$DEST_DIR/android-icon-36x36.png"
generate_favicon 48 "$DEST_DIR/android-icon-48x48.png"
generate_favicon 72 "$DEST_DIR/android-icon-72x72.png"
generate_favicon 96 "$DEST_DIR/android-icon-96x96.png"
generate_favicon 144 "$DEST_DIR/android-icon-144x144.png"
generate_favicon 192 "$DEST_DIR/android-icon-192x192.png"

# Generate apple-touch-icon
generate_favicon 180 "$DEST_DIR/apple-touch-icon-180x180.png"

# Generate PWA icons
generate_favicon 192 "$DEST_DIR/pwa-192x192.png"
generate_favicon 512 "$DEST_DIR/pwa-512x512.png"

# Generate tile icons
generate_favicon 70 "$DEST_DIR/tile70x70.png"
generate_favicon 150 "$DEST_DIR/tile150x150.png"
magick "$PADDED_PNG" -resize 310x150 "$DEST_DIR/tile310x150.png"
generate_favicon 310 "$DEST_DIR/tile310x310.png"

echo "Cleaning up temporary files..."
rm -f "$TEMP_PNG" "$PADDED_PNG" /tmp/favicon-*.png

echo "✓ All missing favicons generated successfully!"
echo "  Output directory: $DEST_DIR"
