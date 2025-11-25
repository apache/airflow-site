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


// Enabled button with 1000px threshold
const scrollToTopBtn = document.getElementById('scrollToTopBtn');
const scrollThreshold = 1000;

function toggleScrollToTopButton() {
  if (!scrollToTopBtn) return;

  const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;

  if (scrollPosition <= scrollThreshold) {
    if (scrollToTopBtn.style.opacity !== '0' && scrollToTopBtn.style.display !== 'none') {
      scrollToTopBtn.style.opacity = '0';
      setTimeout(() => scrollToTopBtn.style.display = 'none', 300);
    }
  } else {
    if (scrollToTopBtn.style.display === 'none') {
      scrollToTopBtn.style.display = 'flex';
      setTimeout(() => scrollToTopBtn.style.opacity = '1', 10);
    }
  }
}

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

window.addEventListener('scroll', toggleScrollToTopButton);
scrollToTopBtn.addEventListener('click', scrollToTop);

scrollToTopBtn.onmouseover = function () {
  this.style.backgroundColor = '#0056b3';
  this.style.transform = 'scale(1.1)';
};

scrollToTopBtn.onmouseout = function () {
  this.style.backgroundColor = '#007bff';
  this.style.transform = 'scale(1)';
};

scrollToTopBtn.addEventListener('mousedown', function () {
  this.style.border = '1.5px solid lightgreen';
});
scrollToTopBtn.addEventListener('mouseup', function () {
  this.style.border = 'none';
});

scrollToTopBtn.addEventListener('focus', function () {
  this.style.outline = '1px solid lightblue';
});
scrollToTopBtn.addEventListener('blur', function () {
  this.style.outline = 'none';
});

toggleScrollToTopButton();