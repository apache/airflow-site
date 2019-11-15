
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
import shuffle from "lodash/shuffle";

function handleIntegration() {
  const root = document.querySelector("#integrations");

  if (!root) {
    return;
  }

  const templateText = root.querySelector("#integration-template").innerText;
  const templateElement = document.createElement("div");
  templateElement.innerHTML = templateText;

  const loadingIndicator = root.querySelector(".loading");
  const listItems = root.querySelector(".list-items");
  const searchBox = root.querySelector('[type="search"]');
  const moreButton = root.querySelector("#show-more-integration");

  let currentPage = 1;
  let currentQeury = "";
  const maxItemsOnPage = window.innerWidth < 1920 ? 8 : 10;

  function setIndicatorVisibility(visible) {
    loadingIndicator.style.display = visible ? "" : "none";
    listItems.style.display = visible ? "none" : "";
  }
  setIndicatorVisibility(false);

  function setMoreButtonVisibility(visible) {
    moreButton.style.display = visible ? "" : "none";
  }
  setMoreButtonVisibility(true);

  const sortByLogoAvailability = (a, b) => {
    const a_key = a.logo ? 1 : -1;
    const b_key = b.logo ? 1 : -1;
    return b_key - a_key;
  };

  let fetchIntegrationRequest = null;

  function fetchIntegration() {
    if (fetchIntegrationRequest) {
      return fetchIntegrationRequest;
    }
    const request = Promise.all([
      fetch("/integrations.json"),
      () => {
        setIndicatorVisibility(true);
      }
    ])
      .then(([resp]) => resp.json())
      .then((integrations) => {
        setIndicatorVisibility(false);
        return Promise.resolve(integrations);
      })
      .then((integrations) => {
        integrations = shuffle(integrations);
        integrations.sort(sortByLogoAvailability);
        integrations.forEach((i, index) => i.inddex = index);
        return Promise.resolve(integrations);
      });
    fetchIntegrationRequest = request;
    return request;
  }

  function createElement(item) {
    const element = templateElement.cloneNode(true);

    const imgNode = element.querySelector('[data-name="logo"]');
    if (item.logo) {
      imgNode.src = item.logo;
      imgNode.alt = `${item.name} logo`;
    } else {
      imgNode.parentNode.removeChild(imgNode);
    }

    element.querySelector('[data-name="name"]').innerText = item.name;
    element.querySelector("a").href = item.url;
    return element.firstElementChild;
  }

  function setItems(items) {
    if (items.length === 0) {
      listItems.innerText = "No items";
    } else {
      while (listItems.firstChild) {
        listItems.removeChild(listItems.firstChild);
      }
      items.forEach((item) => {
        const element = createElement(item);
        listItems.append(element);
      });
    }
  }

  function showItems(keyword, page) {
    const showMoreButtonIfNeeded = (integrations) => {
      setMoreButtonVisibility(integrations.length > (page * maxItemsOnPage));
    };

    const filterMatchingItems = (integrations) => {
      if (!keyword) {
        return Promise.resolve(integrations);
      }
      const selectedIntegration = integrations.filter(
        (integration) => integration.name.toLowerCase().indexOf(keyword.toLowerCase()) >= 0
      );
      return Promise.resolve(selectedIntegration);
    };

    const filterVisible = (integrations) => {
      return Promise.resolve(integrations.slice(0, page * maxItemsOnPage));
    };

    const itemsPromise = fetchIntegration()
      .then(filterMatchingItems);
    itemsPromise.then(filterVisible).then(setItems);
    itemsPromise.then(showMoreButtonIfNeeded);
  }

  function setSearchQuery(keyword) {
    currentQeury = keyword;
    showItems(currentQeury, currentPage);
  }

  searchBox.addEventListener("keyup", debounce(function() {
    currentPage = 1;
    setSearchQuery(searchBox.value);
  }, 0));

  moreButton.addEventListener("click", function() {
    currentPage = currentPage + 1;
    setSearchQuery(searchBox.value);
  });

  setSearchQuery("");
}

handleIntegration();
