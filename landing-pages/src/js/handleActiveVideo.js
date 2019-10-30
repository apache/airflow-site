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

const videosList = document.querySelectorAll(".video-list__item");
const urlHash = window.location.hash;

const addActiveClass = (videoItem) => {
  videosList.forEach((item) => item.classList.remove("active"));
  videoItem.classList.add("active");
};

export const handleActiveVideo = () => {
  if (videosList.length === 0) return;

  urlHash ?
    videosList.forEach((videoLink) => videoLink.hash === urlHash && videoLink.classList.add("active"))
    : videosList[videosList.length - 1].classList.add("active");

  videosList.forEach((item) =>
    item.addEventListener("click", (event) => addActiveClass(event.currentTarget))
  );
};
