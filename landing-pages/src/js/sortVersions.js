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

const splitParts = (ver_a) => {
  const have_release = ver_a.indexOf("-") > 0;
  const have_build = ver_a.indexOf("+") > 0;
  if (have_release && have_build) {
    const [core, rest] = ver_a.split("-", 2);
    const [release, build] = rest.split("+", 2);
    return [core, release, build];
  } else if (have_release) {
    const [core, release] = ver_a.split("-", 2);
    return [core, release, null];
  } else if (have_build) {
    const [core, build] = ver_a.split("+", 2);
    return [core, null, build];
  } else {
    return [ver_a, null, null];
  }
};

const compareCoreVersion = (ver_a, ver_b) => {
  const a = ver_a.split(".");
  const b = ver_b.split(".");

  for (let i = 0; i < Math.min(a.length, b.length); i++) {
    const cmp = a[i] - b[i];
    if (cmp !== 0) {
      return Math.max(-1, Math.min(cmp, 1));
    }
  }
  const cmp = a.length - b.length;
  return Math.max(-1, Math.min(cmp, 1));
};

const compareString = (str_a, str_b) => {
  if (str_a && str_b) {
    return str_a.localeCompare(str_b);
  }
  if (!str_a && !str_b) {
    return 0;
  }
  if (str_a) {
    return -1;
  }
  return 1;
};

export const compareVersion = (ver_a, ver_b) => {
  const [core_a, release_a, build_a] = splitParts(ver_a);
  const [core_b, release_b, build_b] = splitParts(ver_b);

  const cmp_core = compareCoreVersion(core_a, core_b);
  const cmp_release = compareString(release_a, release_b);
  const cmp_build = compareString(build_a, build_b);

  if (cmp_core !== 0) {
    return cmp_core;
  }
  if (cmp_release !== 0) {
    return cmp_release;
  }
  return cmp_build;
};
