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

const itemsOnPage = 8;

const showElementsOnPage = (elements, currentPage) => {
  elements.slice(currentPage * itemsOnPage, (currentPage + 1) * itemsOnPage).map((child) => {
    child.style.display = "";
  });
};

export const showMoreCommiters = (containerID, buttonID) => {
  let currentPage = 1;
  const container = window.document.querySelector(containerID);
  const button = window.document.querySelector(buttonID);
  if (!container || !button) return;
  if (container.childElementCount <= itemsOnPage * currentPage) return;

  button.style.display = "block";
  const commiterElements = Array.from(container.children);
  commiterElements
    .slice(itemsOnPage, container.childElementCount)
    .map((child) => {
      child.style.display = "none";
    });

  button.addEventListener("click", () => {
    showElementsOnPage(commiterElements, currentPage);
    currentPage += 1;
    if (container.childElementCount <= itemsOnPage * currentPage) {
      button.style.display = "none";
    }
  });
};
