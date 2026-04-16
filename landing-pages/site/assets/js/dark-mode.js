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

(() => {
  'use strict'

  const themeKey = 'theme'
  const getStoredTheme = () => localStorage.getItem(themeKey)
  const setStoredTheme = theme => localStorage.setItem(themeKey, theme)

  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
      return storedTheme
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  const setTheme = theme => {
    document.documentElement.setAttribute('data-bs-theme', theme)
  }

  const updateToggle = (theme) => {
    document.querySelectorAll('.theme-toggle-pill__btn').forEach(btn => {
      const isActive = btn.getAttribute('data-theme-value') === theme
      btn.classList.toggle('active', isActive)
      btn.setAttribute('aria-pressed', isActive)
    })
  }

  // Apply theme immediately (before DOM ready) to prevent flash
  setTheme(getPreferredTheme())

  // Follow system preference changes when no explicit choice stored
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    if (!getStoredTheme()) {
      const theme = getPreferredTheme()
      setTheme(theme)
      updateToggle(theme)
    }
  })

  const init = () => {
    updateToggle(getPreferredTheme())

    document.querySelectorAll('.theme-toggle-pill__btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const theme = btn.getAttribute('data-theme-value')
        setStoredTheme(theme)
        setTheme(theme)
        updateToggle(theme)
      })
    })
  }

  if (document.readyState === 'loading') {
    window.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
