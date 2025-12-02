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

const SCROLL_THRESHOLD = 100; // Show button after scrolling 100px

document.addEventListener("DOMContentLoaded", function() {
  const scrollToTopBtn = document.getElementById("scroll-to-top-btn");

  if (!scrollToTopBtn) {
    return; // Button not found on this page
  }

  // Function to toggle button visibility
  function toggleScrollToTopBtn() {
    if (window.scrollY > SCROLL_THRESHOLD) {
      scrollToTopBtn.style.display = "flex";
    } else {
      scrollToTopBtn.style.display = "none";
    }
  }

  // Function to scroll to top smoothly
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  }

  // Add scroll event listener
  window.addEventListener("scroll", toggleScrollToTopBtn);

  // Add click event listener
  scrollToTopBtn.addEventListener("click", scrollToTop);

  // Initialize button visibility on load
  toggleScrollToTopBtn();
});
