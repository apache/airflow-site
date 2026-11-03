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

// Turns runs of sibling `<details name="..." data-tab="...">` elements into a tab set. Without JS they
// remain an exclusive accordion. Tab sets sharing a `data-sync-group` switch together, and the choice is
// stored under the same sessionStorage key as sphinx-design so it carries over to and from the docs.

const TAB_SELECTOR = "details[data-tab]";
const STORAGE_KEY_PREFIX = "sphinx-design-tab-id-";

const readStoredTab = (group) => {
  try {
    return window.sessionStorage.getItem(STORAGE_KEY_PREFIX + group);
  } catch {
    return null;
  }
};

const storeTab = (group, id) => {
  try {
    window.sessionStorage.setItem(STORAGE_KEY_PREFIX + group, id);
  } catch {
    // Storage can be unavailable (private mode, blocked site data); syncing still works on this page.
  }
};

const tabSetByPanel = new WeakMap();
const tabSetsByGroup = new Map();

class TabSet {
  constructor(panels, index) {
    this.panels = panels;
    this.group = panels[0].dataset.syncGroup;

    this.tablist = document.createElement("div");
    this.tablist.className = "tab-set__tabs";
    this.tablist.setAttribute("role", "tablist");
    this.tablist.addEventListener("keydown", (event) => this.onKeydown(event));

    const container = document.createElement("div");
    container.className = "tab-set";
    panels[0].before(container);
    container.append(this.tablist, ...panels);

    this.tabs = panels.map((panel, i) => this.createTab(panel, i, `tab-set-${index}-${i}`));

    const initial = panels.findIndex((panel) => panel.open);
    this.select(initial === -1 ? 0 : initial);
  }

  createTab(panel, i, idPrefix) {
    const tab = document.createElement("button");
    tab.type = "button";
    tab.className = "tab-set__tab";
    tab.id = `${idPrefix}-tab`;
    tab.setAttribute("role", "tab");

    const summary = panel.querySelector(":scope > summary");
    if (summary) {
      tab.append(...summary.cloneNode(true).childNodes);
    } else {
      tab.textContent = panel.dataset.tab;
    }

    if (!panel.id) panel.id = `${idPrefix}-panel`;
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("aria-labelledby", tab.id);
    tab.setAttribute("aria-controls", panel.id);

    tab.addEventListener("click", () => this.activate(i));
    // Browsers open closed details themselves (find-in-page, fragment navigation), so follow along.
    panel.addEventListener("toggle", () => {
      if (panel.open) this.select(i);
    });

    tabSetByPanel.set(panel, {tabSet: this, index: i});
    this.tablist.append(tab);
    return tab;
  }

  select(index) {
    this.panels.forEach((panel, i) => {
      const selected = i === index;
      panel.open = selected;
      this.tabs[i].setAttribute("aria-selected", String(selected));
      this.tabs[i].tabIndex = selected ? 0 : -1;
    });
  }

  selectById(id) {
    const index = this.panels.findIndex((panel) => panel.dataset.tab === id);
    if (index !== -1) this.select(index);
  }

  activate(index) {
    const anchorTop = this.tablist.getBoundingClientRect().top;
    this.select(index);
    if (this.group) {
      const id = this.panels[index].dataset.tab;
      tabSetsByGroup.get(this.group).forEach((tabSet) => {
        if (tabSet !== this) tabSet.selectById(id);
      });
      storeTab(this.group, id);
    }
    // Synced sets above this one change height, so keep the strip the reader clicked where it was.
    const shift = this.tablist.getBoundingClientRect().top - anchorTop;
    if (shift) window.scrollBy({top: shift, behavior: "instant"});
  }

  onKeydown(event) {
    const current = this.tabs.indexOf(event.target);
    if (current === -1) return;
    const last = this.tabs.length - 1;
    const next = {
      ArrowRight: current === last ? 0 : current + 1,
      ArrowLeft: current === 0 ? last : current - 1,
      Home: 0,
      End: last,
    }[event.key];
    if (next === undefined) return;
    event.preventDefault();
    this.activate(next);
    this.tabs[next].focus();
  }
}

const findTabSetRuns = () => {
  const runs = [];
  const runByLastPanel = new Map();
  // Pages can include the bundle more than once, so skip panels a previous run already enhanced.
  document.querySelectorAll(`${TAB_SELECTOR}:not([role="tabpanel"])`).forEach((details) => {
    const name = details.getAttribute("name");
    const previous = details.previousElementSibling;
    const run = runByLastPanel.get(previous);
    if (name && run && previous.getAttribute("name") === name) {
      run.push(details);
      runByLastPanel.delete(previous);
      runByLastPanel.set(details, run);
    } else {
      const newRun = [details];
      runs.push(newRun);
      runByLastPanel.set(details, newRun);
    }
  });
  return runs;
};

const revealFragmentTarget = () => {
  const id = decodeURIComponent(window.location.hash.slice(1));
  const target = id && document.getElementById(id);
  if (!target) return;
  let revealed = false;
  for (let panel = target.closest(TAB_SELECTOR); panel; panel = panel.parentElement.closest(TAB_SELECTOR)) {
    const owner = tabSetByPanel.get(panel);
    if (owner && !panel.open) {
      owner.tabSet.select(owner.index);
      revealed = true;
    }
  }
  if (revealed) target.scrollIntoView();
};

const initDetailsTabs = () => {
  const urlParams = new URLSearchParams(window.location.search);

  findTabSetRuns().forEach((panels, index) => {
    const tabSet = new TabSet(panels, index);
    if (!tabSet.group) return;
    if (!tabSetsByGroup.has(tabSet.group)) {
      tabSetsByGroup.set(tabSet.group, []);
      const fromUrl = urlParams.get(tabSet.group);
      if (fromUrl) storeTab(tabSet.group, fromUrl);
    }
    tabSetsByGroup.get(tabSet.group).push(tabSet);
    const stored = readStoredTab(tabSet.group);
    if (stored) tabSet.selectById(stored);
  });

  revealFragmentTarget();
  window.addEventListener("hashchange", revealFragmentTarget);
};

initDetailsTabs();
