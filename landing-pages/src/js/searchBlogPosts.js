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

import lunr from "lunr";

const query = new URLSearchParams(window.location.search);
const searchString = query.get("q");
document.querySelector("#search").value = searchString;

const $target = document.querySelector(".list-items");

const $itemTemplate = $target.firstElementChild.cloneNode(true);


const formatDate = (date) => {
  const dateOptions = {weekday: "short", year: "numeric", month: "short", day: "numeric"};
  return new Date(date).toLocaleDateString("en-US", dateOptions);
};

const setTags = (tagsContainer, tags) => {
  while (tagsContainer.firstChild) {
    tagsContainer.removeChild(tagsContainer.firstChild);
  }
  tags.forEach((tag) => {
    const tagElement = document.createElement("a");
    tagsContainer.appendChild(tagElement);
    tagElement.setAttribute("class", "tag");
    tagElement.setAttribute("href", `/blog/tags/${tag}/`);
    tagElement.innerText = tag;
  });
};

Promise.all([
  fetch("/_gen/indexes/en/blog-index.json"),
  fetch("/_gen/indexes/en/blog-posts.json")
]).then(function([indexResp, postsResp]) {
  return Promise.all([
    indexResp.json(),
    postsResp.json()
  ]);
}).then(function([index, posts]) {
  const lunrIndex = lunr.Index.load(index);
  const matches = lunrIndex.search(searchString);
  const results = [];
  matches.forEach(function(match) {
    posts.filter((post) => post.title === match.ref)
      .forEach((post) => {
        results.push({post, match});
      });
  });
  results.sort((a, b) => a.match.score - b.match.score);

  if (results.length > 10) {
    results.splice(10, results.length - 10);
  }

  if (results.length > 0) {
    while ($target.firstChild) {
      $target.removeChild($target.firstChild);
    }
    results.forEach((result) => {
      const $newResultItem = $itemTemplate.cloneNode(true);
      $newResultItem.querySelector(".box-event__blogpost--header").innerText = result.post.title;
      $newResultItem.querySelector(".box-event__blogpost--author").innerText = result.post.author;
      $newResultItem.querySelector(".box-event__blogpost--description").innerText = result.post.description;
      $newResultItem.querySelector(".box-event__blogpost--date").innerText = formatDate(result.post.date);
      setTags($newResultItem.querySelector(".box-event__blogpost--metadata > .tags-container"), result.post.tags);
      $newResultItem.querySelector(".box-event__blogpost > a").href = `/blog/${result.post.url}/`;
      $target.append($newResultItem);
    });
  } else {
    $target.innerHTML = "<div>No search results found</div>";
  }
});
