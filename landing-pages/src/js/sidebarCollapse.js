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

const handleClick = (section) => {
  const subsection = section.querySelector(".collapse");
  if (subsection.classList.contains("show")) {
    subsection.classList.remove("show");
    // section.classList.remove("arrow-down");
  } else {
    subsection.classList.add("show");
    // section.classList.add("arrow-down");
  }
};

const handleCollapse = () => {
  const root = window.document.querySelector(".roadmap");
  if (!root) {
    return;
  }

  const arrows = root.querySelectorAll(".td-sidebar-nav > .td-sidebar-nav__section .td-sidebar-nav__section");
  arrows.forEach(section => section.addEventListener("click", () => handleClick(section)));
};

handleCollapse();
