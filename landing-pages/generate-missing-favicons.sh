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

echo "Converting SVG to high-resolution PNG..."
rsvg-convert -w 1024 -h 1024 "$SOURCE_SVG" -o "$TEMP_PNG"

echo "Generating ALL favicon files..."

# Generate standard favicon sizes
magick "$TEMP_PNG" -resize 16x16 "$DEST_DIR/favicon-16x16.png"
magick "$TEMP_PNG" -resize 32x32 "$DEST_DIR/favicon-32x32.png"
magick "$TEMP_PNG" -resize 96x96 "$DEST_DIR/favicon-96x96.png"
magick "$TEMP_PNG" -resize 256x256 "$DEST_DIR/favicon-256.png"
cp "$TEMP_PNG" "$DEST_DIR/favicon-1024.png"

# Generate favicon.ico with multiple sizes (16, 32, 48)
magick "$TEMP_PNG" -resize 16x16 /tmp/favicon-16.png
magick "$TEMP_PNG" -resize 32x32 /tmp/favicon-32.png
magick "$TEMP_PNG" -resize 48x48 /tmp/favicon-48.png
magick /tmp/favicon-16.png /tmp/favicon-32.png /tmp/favicon-48.png "$DEST_DIR/favicon.ico"

# Generate android-* files (without -icon- in name)
magick "$TEMP_PNG" -resize 36x36 "$DEST_DIR/android-36x36.png"
magick "$TEMP_PNG" -resize 48x48 "$DEST_DIR/android-48x48.png"
magick "$TEMP_PNG" -resize 72x72 "$DEST_DIR/android-72x72.png"
magick "$TEMP_PNG" -resize 96x96 "$DEST_DIR/android-96x96.png"
magick "$TEMP_PNG" -resize 144x144 "$DEST_DIR/android-144x144.png"
magick "$TEMP_PNG" -resize 192x192 "$DEST_DIR/android-192x192.png"

# Generate android-icon-* files (with -icon- in name)
magick "$TEMP_PNG" -resize 36x36 "$DEST_DIR/android-icon-36x36.png"
magick "$TEMP_PNG" -resize 48x48 "$DEST_DIR/android-icon-48x48.png"
magick "$TEMP_PNG" -resize 72x72 "$DEST_DIR/android-icon-72x72.png"
magick "$TEMP_PNG" -resize 96x96 "$DEST_DIR/android-icon-96x96.png"
magick "$TEMP_PNG" -resize 144x144 "$DEST_DIR/android-icon-144x144.png"
magick "$TEMP_PNG" -resize 192x192 "$DEST_DIR/android-icon-192x192.png"

# Generate apple-touch-icon
magick "$TEMP_PNG" -resize 180x180 "$DEST_DIR/apple-touch-icon-180x180.png"

# Generate PWA icons
magick "$TEMP_PNG" -resize 192x192 "$DEST_DIR/pwa-192x192.png"
magick "$TEMP_PNG" -resize 512x512 "$DEST_DIR/pwa-512x512.png"

# Generate tile icons
magick "$TEMP_PNG" -resize 70x70 "$DEST_DIR/tile70x70.png"
magick "$TEMP_PNG" -resize 150x150 "$DEST_DIR/tile150x150.png"
magick "$TEMP_PNG" -resize 310x150 "$DEST_DIR/tile310x150.png"
magick "$TEMP_PNG" -resize 310x310 "$DEST_DIR/tile310x310.png"

echo "Cleaning up temporary files..."
rm -f "$TEMP_PNG" /tmp/favicon-*.png

echo "✓ All missing favicons generated successfully!"
echo "  Output directory: $DEST_DIR"
