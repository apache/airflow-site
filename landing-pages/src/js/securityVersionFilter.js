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

/*
 * Version filter on the /security/<product>/ pages. Each table row carries
 * data-affected: a JSON list of {from, lt, le} ranges ("" = unbounded) built
 * from the affected versions of the record. Typing a version hides the rows
 * whose ranges do not contain it. The state is kept in ?version=&package= so a
 * filtered view can be linked to.
 */

const VERSION_RE = /^\s*v?(\d+(?:\.\d+)*)\s*$/;

// "2.10.5" -> [2, 10, 5]; anything else -> null. Pre-release suffixes are not
// accepted: the records only carry release versions.
export function parseVersion(text) {
  const match = VERSION_RE.exec(text || "");
  return match ? match[1].split(".").map(Number) : null;
}

export function compareVersions(a, b) {
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    const diff = (a[i] || 0) - (b[i] || 0);
    if (diff) {
      return diff;
    }
  }
  return 0;
}

export function rangeContains(range, version) {
  const from = parseVersion(range.from);
  if (from && compareVersions(version, from) < 0) {
    return false;
  }
  const lt = parseVersion(range.lt);
  if (lt) {
    return compareVersions(version, lt) < 0;
  }
  const le = parseVersion(range.le);
  if (le) {
    return compareVersions(version, le) <= 0;
  }
  return Boolean(from);
}

function setupFilter(form) {
  const versionInput = form.querySelector("[name=version]");
  const packageSelect = form.querySelector("[name=package]");
  const status = form.querySelector(".security-version-filter__status");
  const container = form.parentElement;
  const sections = [...container.querySelectorAll(".security-package")];
  const packageIndex = container.querySelector(".security-packages-index");
  const tables = [...container.querySelectorAll("table.security-cves")];
  const rows = [...container.querySelectorAll("tr[data-affected]")].map((row) => {
    let ranges = [];
    try {
      ranges = JSON.parse(row.dataset.affected);
    } catch {
      ranges = [];
    }
    return {row, ranges};
  });

  // One "nothing matches" note per table, shown when all its rows are hidden.
  const emptyNotes = tables.map((table) => {
    const note = document.createElement("p");
    note.className = "security-version-filter__empty";
    note.hidden = true;
    table.closest(".table-responsive").after(note);
    return note;
  });

  function syncUrl(versionText, pkg) {
    const params = new URLSearchParams(window.location.search);
    versionText ? params.set("version", versionText) : params.delete("version");
    pkg ? params.set("package", pkg) : params.delete("package");
    const query = params.toString();
    window.history.replaceState(null, "", `${window.location.pathname}${query ? `?${query}` : ""}${window.location.hash}`);
  }

  function apply() {
    const versionText = versionInput.value.trim();
    const pkg = packageSelect ? packageSelect.value : "";
    const version = parseVersion(versionText);
    // Provider versions only mean something for one package at a time.
    const needsPackage = Boolean(packageSelect) && !pkg;
    const filtering = Boolean(version) && !needsPackage;

    versionInput.setAttribute("aria-invalid", String(Boolean(versionText) && !version));
    sections.forEach((section) => {
      section.hidden = Boolean(pkg) && section.dataset.package !== pkg;
    });
    if (packageIndex) {
      packageIndex.hidden = Boolean(pkg);
    }

    let shown = 0;
    let total = 0;
    rows.forEach(({row, ranges}) => {
      const visibleSection = !row.closest(".security-package") || !row.closest(".security-package").hidden;
      // A row without ranges cannot be ruled out, so it stays visible.
      const matches = !filtering || ranges.length === 0 || ranges.some((range) => rangeContains(range, version));
      row.hidden = !matches;
      if (visibleSection) {
        total += 1;
        shown += matches ? 1 : 0;
      }
    });

    tables.forEach((table, i) => {
      const anyVisible = [...table.tBodies[0].rows].some((row) => !row.hidden);
      table.closest(".table-responsive").hidden = !anyVisible;
      emptyNotes[i].hidden = anyVisible;
      emptyNotes[i].textContent = anyVisible ? "" : `No published CVE affects version ${versionText}.`;
    });

    if (versionText && !version) {
      status.textContent = "Enter a version number, for example 2.10.5.";
    } else if (version && needsPackage) {
      status.textContent = "Choose a provider package: each provider has its own version numbers.";
    } else if (filtering) {
      const subject = pkg ? `${pkg} ${versionText}` : `version ${versionText}`;
      status.textContent = shown === 0 ?
        `No published CVE affects ${subject}.` :
        `${shown} of ${total} CVEs affect ${subject}.`;
    } else {
      status.textContent = "";
    }
    syncUrl(versionText, pkg);
  }

  const params = new URLSearchParams(window.location.search);
  versionInput.value = params.get("version") || "";
  if (packageSelect) {
    const pkg = params.get("package") || "";
    packageSelect.value = [...packageSelect.options].some((o) => o.value === pkg) ? pkg : "";
  }

  form.addEventListener("submit", (event) => event.preventDefault());
  form.addEventListener("input", apply);
  form.addEventListener("change", apply);
  // The form resets its fields after the event, so filter once that is done.
  form.addEventListener("reset", () => window.setTimeout(apply));

  form.hidden = false;
  apply();
}

document.querySelectorAll(".security-version-filter").forEach(setupFilter);
