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

/* global ga */

const handleFeedback = () => {
  const rating = window.document.querySelector(".rating");

  if (!rating) return;

  const sendFeedback = (value) => {
    if (typeof ga !== "function") return;
    const args = {
      command: "send",
      hitType: "event",
      category: "Helpful",
      action: "click",
      label: window.location.pathname,
      value: value
    };
    ga(args.command, args.hitType, args.category, args.action, args.label, args.value);
  };

  const displayMessage = () => {
    rating.innerHTML = "<p class='bodytext__medium--brownish-grey font-weight-500 mb-0'>Thank you!</p>";
  };

  for (let i = 1; i <= 5; i++) {
    rating.querySelector(`#rate-star-${i}`).addEventListener("click", () => {
      sendFeedback(i);
      displayMessage();
    });
  }
};

handleFeedback();
