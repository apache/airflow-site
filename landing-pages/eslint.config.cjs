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

const globals = require("globals");
const pluginJs = require("@eslint/js");
const importPlugin = require("eslint-plugin-import");

module.exports = [
  {
    ignores: [
      "node_modules/**",
      "dist/**",
      "site/**",
      "**/*.min.js",
      "**/vendor/**",
    ],
  },
  // Configuration for Node.js files (webpack configs, build scripts)
  {
    files: ["webpack.*.js", "create-index.js", "postcss.config.js"],
    languageOptions: {
      globals: {
        ...globals.node,
      },
      ecmaVersion: 2020,
      sourceType: "commonjs",
    },
    rules: {
      "no-console": "off", // Allow console in build scripts
      "no-unused-vars": ["error", {"args": "none"}],
    },
  },
  // Configuration for browser JavaScript
  {
    files: ["src/**/*.js"],
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.es6,
      },
      ecmaVersion: 2020,
      sourceType: "module",
    },
    plugins: {
      import: importPlugin,
    },
    rules: {
      // Possible Errors
      "no-control-regex": "error",
      "no-console": "warn",
      "no-debugger": "error",
      "no-dupe-args": "error",
      "no-dupe-keys": "error",
      "no-duplicate-case": "error",
      "no-empty-character-class": "error",
      "no-ex-assign": "error",
      "no-extra-boolean-cast": "error",
      "no-extra-semi": "error",
      "no-invalid-regexp": "error",
      "no-irregular-whitespace": "warn",
      "no-proto": "error",
      "no-unexpected-multiline": "error",
      "no-unreachable": "error",
      "valid-typeof": "error",

      // Best Practices
      "no-fallthrough": "error",
      "no-redeclare": "error",

      // Stylistic Issues
      "comma-spacing": "error",
      "eol-last": "error",
      "eqeqeq": ["error", "smart"],
      "indent": ["error", 2, {SwitchCase: 1}],
      "keyword-spacing": "error",
      "max-len": ["warn", 160, 2],
      "new-parens": "error",
      "no-mixed-spaces-and-tabs": "error",
      "no-multiple-empty-lines": ["error", {max: 2}],
      "no-trailing-spaces": "error",
      "object-curly-spacing": ["error", "never"],
      "quotes": ["error", "double", "avoid-escape"],
      "semi": "error",
      "space-before-blocks": ["error", "always"],
      "space-before-function-paren": ["error", "never"],
      "space-in-parens": ["error", "never"],
      "space-infix-ops": "error",
      "space-unary-ops": "error",

      // ECMAScript 6
      "arrow-parens": ["error", "always"],
      "arrow-spacing": ["error", {"before": true, "after": true}],
      "no-confusing-arrow": "error",
      "prefer-const": "error",

      // Import
      "import/no-unresolved": "off", // Disable for now due to p5 import issues
      "import/export": "error",

      // Variables
      "no-undef": "error",
      "no-unused-vars": ["error", {"args": "none"}],
    },
  },
];
