/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import {compareVersion} from "./sortVersions";

export function initVersionSelector({versions}) {
  const input = document.getElementById("versionInput");
  const suggestionBox = document.getElementById("versionSuggestions");

  if (!input || !suggestionBox || !versions) {
    return;
  }

  // Sort versions newest → oldest (copy, original array ko mat chhedo)
  const sortedVersions = versions.slice().sort(compareVersion).reverse();

  // Show suggestions
  function showSuggestions(filtered) {
    suggestionBox.innerHTML = "";

    if (filtered.length === 0) {
      suggestionBox.style.display = "none";
      return;
    }

    filtered.forEach((v) => {
      const item = document.createElement("div");
      item.className = "version-suggestion-item";
      item.textContent = v;

      item.addEventListener("click", () => {
        goToVersion(v);
      });

      suggestionBox.appendChild(item);
    });

    suggestionBox.style.display = "block";
  }

  // Handle input typing
  input.addEventListener("input", () => {
    const query = input.value.toLowerCase();
    const filtered = sortedVersions.filter((v) =>
      v.toLowerCase().includes(query)
    );
    showSuggestions(filtered);
  });

  // Enter key → go to version
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      goToVersion(input.value.trim());
    }
  });

  function goToVersion(version) {
    if (!version) {
      return;
    }

    const parts = window.location.pathname.split("/");
    // /docs/<package>/<version>/page...
    const pkg = parts[2] || "";
    const pagePath = parts.slice(4).join("/");

    window.location.href = `/docs/${pkg}/${version}/${pagePath}`;
  }

  // Hide suggestion box on click outside
  document.addEventListener("click", (e) => {
    if (!e.target.closest("#docs-version-selector")) {
      suggestionBox.style.display = "none";
    }
  });
}
