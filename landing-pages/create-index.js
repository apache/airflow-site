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

/* eslint-disable no-console */

const fs = require("fs").promises;
const path = require("path");
const {promisify} = require("util");
const frontMatterParser = require("parser-front-matter");
const parse = promisify(frontMatterParser.parse.bind(frontMatterParser));
const lunrjs = require("lunr");

const contentDirectory = `${__dirname}/site/content`;
const outputtDirectory = `${__dirname}/site/static/_gen/indexes`;


async function isDirectoryExists(dirPath) {
  try {
    if ((await fs.stat(dirPath)).isDirectory()) {
      return true;
    }
  } catch (err) {
    return false;
  }
  return false;
}

async function loadPostsWithFrontMatter(postsDirectoryPath) {
  const fileNames = await fs.readdir(postsDirectoryPath);
  const posts = await Promise.all(
    fileNames.map(async(fileName) => {
      let filePath;
      if ((await fs.stat(`${postsDirectoryPath}/${fileName}`)).isFile()) {
        filePath = `${postsDirectoryPath}/${fileName}`;
      } else {
        filePath = `${postsDirectoryPath}/${fileName}/index.md`;
      }
      const fileContent = await fs.readFile(
        filePath,
        "utf8"
      );
      const {content, data} = await parse(fileContent);
      return {
        content: content.slice(0, 3000),
        url: path.parse(fileName).name,
        ...data
      };
    })
  );
  return posts;
}

function makeIndex(posts) {
  return lunrjs(function() {
    this.ref("title");
    this.field("title");
    this.field("description");
    this.field("author");
    this.field("content");
    this.field("tags");
    this.field("url");
    posts.forEach((p) => {
      this.add(p);
    });
  });
}

async function writeJson(filePath, index) {
  await fs.writeFile(filePath, JSON.stringify(index));
  console.log(`Saved ${path.parse(filePath).base} file.`);
}

async function processLanguage(language) {
  console.log(`Proccessing "${language}" language.`);
  const currentDirectory = `${contentDirectory}/${language}/blog`;
  if (!await isDirectoryExists(currentDirectory)) {
    console.log("No blog posts. Skipping.");
    return;
  }
  const posts = await loadPostsWithFrontMatter(currentDirectory);
  const index = makeIndex(posts);
  const currentOutputDirectory = `${outputtDirectory}/${language}`;
  if (!await isDirectoryExists(currentOutputDirectory)) {
    await fs.mkdir(currentOutputDirectory);
  }
  await writeJson(`${currentOutputDirectory}/blog-index.json`, index);
  await writeJson(`${currentOutputDirectory}/blog-posts.json`, posts);
}

async function run() {
  const directoryNames = await fs.readdir(contentDirectory);
  for (const directoryName of directoryNames) {
    await processLanguage(directoryName);
  }
}

run()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error.stack);
    process.exit(1);
  });
