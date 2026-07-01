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

const AIRFLOW_PACKAGE = "apache-airflow";
const STABLE_KEY = "stable";

const getCurrentPageInfo = () => {

  const [, , currentPackageName, currentVersion, ...pagePathParts] = document.location.pathname.split("/");
  const pagePath = pagePathParts.join("/");
  return {currentVersion, currentPackageName, pagePath};
};

// Only the main airflow package gets the "Airflow N" major prefix; providers have self-explanatory versioning.
const updateToggleLabel = (versionSelector, currentPackageName, currentVersion, stableVersion) => {
  if (currentPackageName !== AIRFLOW_PACKAGE) {
    return;
  }
  const resolvedVersion = currentVersion === STABLE_KEY ? stableVersion : currentVersion;
  const major = resolvedVersion.split(".")[0];
  if (!/^\d+$/.test(major)) {
    return;
  }
  const label = versionSelector.querySelector(".version-label");
  const version = versionSelector.querySelector(".version");
  if (label && version) {
    label.textContent = `Airflow ${major} · `;
    version.textContent = resolvedVersion;
  }
};

const updateVersionSelector = (versionSelector, packageAllVersions, stableVersion) => {
  const templateText = versionSelector.querySelector("#version-item-template").innerText;
  let templateElement = document.createElement("div");
  templateElement.innerHTML = templateText;
  templateElement = templateElement.firstElementChild;

  const versionList = versionSelector.querySelector(".version-list");
  const filterInput = versionSelector.querySelector(".version-filter");
  const emptyState = versionSelector.querySelector(".version-empty-state");

  const {currentPackageName, currentVersion, pagePath} = getCurrentPageInfo();
  updateToggleLabel(versionSelector, currentPackageName, currentVersion, stableVersion);

  const appendNewVersionLink = (targetVersion, label, matchVersion) => {
    const newElement = templateElement.cloneNode(true);
    const newDocsLink = `/docs/${currentPackageName}/${targetVersion}/${pagePath}`;
    newElement.setAttribute("href", newDocsLink);
    newElement.setAttribute("data-version", targetVersion);
    // Filter compares against ``data-match-version`` — for the "stable" alias this holds the actual version.
    newElement.setAttribute("data-match-version", matchVersion);
    newElement.innerText = label;
    if (targetVersion === currentVersion) {
      newElement.classList.add("active");
      newElement.setAttribute("aria-current", "true");
    }
    versionList.appendChild(newElement);
  };

  appendNewVersionLink(STABLE_KEY, `Stable (${stableVersion})`, stableVersion);
  packageAllVersions.forEach((version) => appendNewVersionLink(version, version, version));

  if (!filterInput) {
    return;
  }

  const dropdownItems = () => Array.from(versionList.querySelectorAll(".dropdown-item"));

  const applyFilter = (rawQuery) => {
    const query = rawQuery.trim().toLowerCase();
    let visibleCount = 0;
    dropdownItems().forEach((item) => {
      const matchVersion = (item.getAttribute("data-match-version") || "").toLowerCase();
      // Prefix match so typing "1." shows 1.x releases (not 3.11.x which contains "1." as substring).
      const match = query === "" || matchVersion.startsWith(query);
      item.hidden = !match;
      if (match) {
        visibleCount += 1;
      }
    });
    if (emptyState) {
      emptyState.hidden = visibleCount > 0;
    }
  };

  filterInput.addEventListener("input", (event) => applyFilter(event.target.value));

  const toggle = versionSelector.querySelector(".dropdown-toggle");
  if (toggle) {
    toggle.addEventListener("click", () => {
      window.requestAnimationFrame(() => filterInput.focus());
    });
  }

  filterInput.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      if (filterInput.value) {
        filterInput.value = "";
        applyFilter("");
      } else if (toggle) {
        toggle.click();
      }
    } else if (event.key === "Enter") {
      const firstVisible = dropdownItems().find((item) => !item.hidden);
      if (firstVisible) {
        event.preventDefault();
        firstVisible.click();
      }
    }
  });
};

const runVersionSelector = () => {
  const versionSelectors = window.document.querySelectorAll(".docs-version-selector");

  if (!versionSelectors || versionSelectors.length === 0) {
    return;
  }

  fetch("/_gen/packages-metadata.json")
    .then((resp) => resp.json())
    .then((packageInfos) => {
      const {currentPackageName} = getCurrentPageInfo();
      const currentPackageInfo = packageInfos.find((d) => d["package-name"] === currentPackageName);
      if (!currentPackageInfo) {
        return;
      }

      const packageAllVersions = currentPackageInfo["all-versions"].sort(compareVersion).reverse();
      const stableVersion = currentPackageInfo["stable-version"];
      versionSelectors.forEach((d) => updateVersionSelector(d, packageAllVersions, stableVersion));
    });
};

runVersionSelector();
