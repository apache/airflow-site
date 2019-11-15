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

const runVersionSelector = () => {
  const versionSelectors = window.document.querySelectorAll(".docs-version-selector");

  if (!versionSelectors || versionSelectors.length === 0) {
    return;
  }

  fetch("/_gen/docs-index.json")
    .then((resp) => resp.json())
    .then(({stable, versions}) => {
      versions = versions.sort(compareVersion).reverse();
      versionSelectors.forEach((versionSelector) => {
        const templateText = versionSelector.querySelector("#version-item-template").innerText;
        let templateElement = document.createElement("div");
        templateElement.innerHTML = templateText;
        templateElement = templateElement.firstElementChild;

        const dropdownMenu = versionSelector.querySelector(".dropdown-menu");


        const currentVersion = window.document.location.pathname.split("/")[2];

        const appendNewVersionLink = (location, label) => {
          const newElement = templateElement.cloneNode(true);
          const newDocsLink = document.location.toString().replace(
            `/${currentVersion}/`, `/${location}/`
          );
          newElement.setAttribute("href", newDocsLink);
          newElement.innerText = label;
          dropdownMenu.appendChild(newElement);
        };
        appendNewVersionLink("stable", `Stable (${stable})`);
        versions.forEach((version) => appendNewVersionLink(version, version));
      });
    });
};

runVersionSelector();
