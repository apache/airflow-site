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

import debounce from "lodash/debounce";

const contentRoot = window.document.querySelector(".rst-content");
const sideNavRoot = window.document.querySelector(".wy-nav-side-toc");

let currentActive = null;

const runProgressTracking = () => {
  if (!contentRoot || !sideNavRoot) return;

  const sectionsOffsets = [];
  contentRoot.querySelectorAll(".section").forEach((element) => sectionsOffsets.push({
    id: element.id,
    offset: element.offsetTop
  }));

  const handleActiveSection = () => {
    const lastActive = currentActive;
    const currentActiveIndex = Math.max(
      sectionsOffsets.findIndex((section) => section.offset - window.scrollY + 123 > 0) - 1,
      0
    );
    currentActive = sectionsOffsets[currentActiveIndex];

    if (lastActive) {
      const anchor = sideNavRoot.querySelector(`[href='#${lastActive.id}']`);
      anchor && anchor.closest("li").classList.remove("current");
    }
    if (currentActive) {
      const anchor = sideNavRoot.querySelector(`[href='#${currentActive.id}']`);
      anchor.closest("li").classList.add("current");
    }
  };

  window.addEventListener("scroll", debounce(handleActiveSection, 100));
  handleActiveSection();
};

runProgressTracking();
