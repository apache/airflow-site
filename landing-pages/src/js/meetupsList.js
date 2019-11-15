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
  const maxItemsOnPage = window.innerWidth < 1920 ? 8 : 10;

  fetch("/meetups.json")
    .then((response) => response.json())
    .then((allMeetups) => {

      const setMoreButtonVisibility = (visible) => {
        moreButton.style.display = visible ? "" : "none";
      };

      setMoreButtonVisibility(true);

      const sortByIndex = (a, b) => {
        return a.index - b.index;
      };

      const createElement = (item) => {
        const element = templateElement.cloneNode(true);
        const nextMeetupNode = element.querySelector(".box-event__meetup--next-meetup");
        element.querySelector('[data-name="location"]').innerHTML = `${item.city}<br/>${item.country}`;
        element.querySelector('[data-name="members-count"]').innerText = `${item.members} members`;
        element.querySelector("a").href = item.url;

        if (item.date) {
          element.querySelector('[data-name="date"]').innerText = item.date;
        } else {
          nextMeetupNode.innerHTML = "No upcoming meetups";
        }

        return element.firstElementChild;
      };

      const setItems = (items) => {
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
      };

      const showItems = (keyword, page) => {
        const showMoreButtonIfNeeded = (meetups) => {
          setMoreButtonVisibility(meetups.length > (page * maxItemsOnPage));
        };

        const filterMatchingItems = (meetups) => {
          if (!keyword) {
            return meetups;
          }
          return meetups.filter((meetup) =>
            meetup.city.toLowerCase().indexOf(keyword.toLowerCase()) >= 0 ||
            meetup.country.toLowerCase().indexOf(keyword.toLowerCase()) >= 0 ||
            (meetup.continent && meetup.continent.toLowerCase().indexOf(keyword.toLowerCase()) >= 0)
          );
        };

        const filterVisible = (meetups) => {
          meetups.sort(sortByIndex);
          return meetups.slice(0, page * maxItemsOnPage);
        };
        const matchingItems = filterMatchingItems(allMeetups);
        const visibleItems = filterVisible(matchingItems);
        setItems(visibleItems);
        showMoreButtonIfNeeded(matchingItems);
      };

      const setSearchQuery = (keyword) => {
        currentQuery = keyword;
        showItems(currentQuery, currentPage);
      };

      searchBox.addEventListener("keyup", () => {
        currentPage = 1;
        setSearchQuery(searchBox.value);
      });

      moreButton.addEventListener("click", () => {
        currentPage = currentPage + 1;
        setSearchQuery(searchBox.value);
      });

      setSearchQuery("");
    });
};

runMeetups();
