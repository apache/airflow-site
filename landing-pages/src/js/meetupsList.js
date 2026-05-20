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


const MEETUPS_REFRESH_INTERVAL_MS = 5 * 60 * 1000;

const runMeetups = () => {
  const root = document.querySelector(".meetups");

  if (!root) {
    return;
  }

  const templateText = root.querySelector("#meetup-template").innerText;
  const templateElement = document.createElement("div");
  templateElement.innerHTML = templateText;

  const listItems = root.querySelector(".list-items");
  const searchBox = root.querySelector("[type='search']");
  const moreButton = root.querySelector(".more");

  let currentPage = 1;
  let currentQuery = "";
  let allMeetups = [];

  const maxItemsOnPage = window.innerWidth < 1920 ? 8 : 10;

  const setMoreButtonVisibility = (visible) => {
    moreButton.style.display = visible ? "" : "none";
  };

  const sortByIndex = (a, b) => {
    return a.index - b.index;
  };

  const createElement = (item) => {
    const element = templateElement.cloneNode(true);
    element.querySelector('[data-name="location"]').innerHTML = `${item.city}<br/>${item.country}`;
    element.querySelector('[data-name="members-count"]').innerText = `${item.members} members`;
    element.querySelector("a").href = item.url;

    return element.firstElementChild;
  };

  const setItems = (items) => {
    while (listItems.firstChild) {
      listItems.removeChild(listItems.firstChild);
    }

    if (items.length === 0) {
      listItems.innerText = "No items";
      return;
    }

    items.forEach((item) => {
      const element = createElement(item);
      listItems.append(element);
    });
  };

  const filterMatchingItems = (meetups, keyword) => {
    if (!keyword) {
      return meetups;
    }

    return meetups.filter((meetup) =>
      meetup.city.toLowerCase().includes(keyword.toLowerCase()) ||
      meetup.country.toLowerCase().includes(keyword.toLowerCase()) ||
      (meetup.continent && meetup.continent.toLowerCase().includes(keyword.toLowerCase()))
    );
  };

  const filterVisible = (meetups, page) => {
    return meetups.sort(sortByIndex).slice(0, page * maxItemsOnPage);
  };

  const showItems = () => {
    const matchingItems = filterMatchingItems(allMeetups, currentQuery);
    const visibleItems = filterVisible(matchingItems, currentPage);

    setItems(visibleItems);
    setMoreButtonVisibility(matchingItems.length > currentPage * maxItemsOnPage);
  };

  const loadMeetups = async() => {
    const response = await fetch(`/meetups.json?updated=${Date.now()}`);

    if (!response.ok) {
      throw new Error("Unable to refresh meetup events");
    }

    const meetups = await response.json();

    if (!Array.isArray(meetups)) {
      throw new Error("Invalid meetup events response");
    }

    allMeetups = meetups;
    showItems();
  };

  searchBox.addEventListener("keyup", () => {
    currentPage = 1;
    currentQuery = searchBox.value;
    showItems();
  });

  moreButton.addEventListener("click", () => {
    currentPage += 1;
    showItems();
  });

  loadMeetups().catch(() => {
    setItems([]);
    setMoreButtonVisibility(false);
  });

  window.setInterval(() => {
    loadMeetups().catch(() => {
      // Keep currently rendered meetup events if a background refresh fails.
    });
  }, MEETUPS_REFRESH_INTERVAL_MS);
};

runMeetups();
