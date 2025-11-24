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

import { compareVersion } from "./sortVersions";

export function initVersionSelector(options) {
  const versions = options.versions;
  const input = document.getElementById("versionInput");
  const suggestionBox = document.getElementById("versionSuggestions");

  if (!input || !suggestionBox || !versions) {
    return;
  }

  const sortedVersions = versions.sort(compareVersion).reverse();

  function goToVersion(version) {
    if (!version) {
      return;
    }

    const parts = window.location.pathname.split("/");
    const pkg = parts[2] || "";
    const pagePath = parts.slice(4).join("/");

    window.location.href = "/docs/" + pkg + "/" + version + "/" + pagePath;
  }

  function showSuggestions(list) {
    suggestionBox.innerHTML = "";

    if (list.length === 0) {
      suggestionBox.style.display = "none";
      return;
    }

    list.forEach(function (v) {
      const item = document.createElement("div");
      item.className = "version-suggestion-item";
      item.textContent = v;

      item.addEventListener("click", function () {
        goToVersion(v);
      });

      suggestionBox.appendChild(item);
    });

    suggestionBox.style.display = "block";
  }

  input.addEventListener("input", function () {
    const query = input.value.toLowerCase();
    const filtered = sortedVersions.filter(function (v) {
      return v.toLowerCase().includes(query);
    });
    showSuggestions(filtered);
  });

  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      goToVersion(input.value.trim());
    }
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest("#docs-version-selector")) {
      suggestionBox.style.display = "none";
    }
  });
}
