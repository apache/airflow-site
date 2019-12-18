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

import * as p5 from "p5";
import debounce from "lodash/debounce";
import {documentReady} from "./utils.js";

const BLOCK_COUNT_X = 7;
const BLOCK_COUNT_Y = 7;
const MAX_BLOCK_SIZE = 30;
const ANIM_SPEED = 0.1;
const ANIM_AMPLITUDE = 40;
const DRAW_SAFE_AREA = false;

const randomBetween = (from, to) => from + Math.random() * (to - from);
const randomInt = (from, to) => Math.round(randomBetween(from, to));
const randomItem = (arr) => arr[randomInt(0, arr.length - 1)];

class Polygon {
  constructor(pos, vectors) {
    this.pos = pos;
    this.vectors = vectors;
  }

  draw(sketch) {
    sketch.push();
    sketch.noStroke();
    sketch.fill(128, 128, 128);
    sketch.translate(this.pos.x, this.pos.y);

    sketch.beginShape();

    for (let i = 0; i < this.vectors.length; i += 1) {
      const v = this.vectors[i];
      sketch.vertex(v.x, v.y);
    }

    sketch.endShape(p5.CLOSE);
    sketch.pop();
  }

  isVectorInside(vector) {
    const vs = this.vectors;
    const x = vector.x - this.pos.x,
      y = vector.y - this.pos.y;

    let inside = false;
    for (let i = 0, j = vs.length - 1; i < vs.length; j = i++) {
      const intersect =
                vs[i].y > y !== vs[j].y > y &&
                x < (vs[j].x - vs[i].x) * (y - vs[i].y) / (vs[j].y - vs[i].y) + vs[i].x;
      if (intersect) inside = !inside;
    }
    return inside;
  }

  calcArea() {
    let total = 0;

    for (let i = 0, l = this.vectors.length; i < l; i++) {
      const addX = this.vectors[i].x;
      const addY = this.vectors[i === this.vectors.length - 1 ? 0 : i + 1].y;
      const subX = this.vectors[i === this.vectors.length - 1 ? 0 : i + 1].x;
      const subY = this.vectors[i].y;

      total += addX * addY * 0.5;
      total -= subX * subY * 0.5;
    }

    return Math.abs(total);
  }
}

class Box {
  constructor(pos, size, color, scale, direction, rotate) {
    this.pos = pos;
    this.size = size;
    this.color = color;
    this.scale = scale;
    this.rotate = rotate;
    this.direction = direction;
    this.shift = null;
    this.animFrame = Math.random() * 100;
  }

  calc(sketch) {
    if (!this.shift) {
      this.shift = sketch.createVector(0, 0);
    }

    this.animFrame += ANIM_SPEED;
    this.rotate = this.animFrame / 50 * sketch.PI;
    this.shift.x =
            Math.cos(this.animFrame / 10) *
            Math.sin(this.animFrame / 10) *
            ANIM_AMPLITUDE;
    this.shift.y = Math.sin(this.animFrame / 10) * ANIM_AMPLITUDE;
  }

  draw(sketch) {
    sketch.push();
    sketch.noStroke();
    sketch.fill(this.color);
    sketch.translate(this.pos.x, this.pos.y);
    sketch.scale(this.scale);
    sketch.translate(this.shift.x, this.shift.y);
    sketch.rotate(this.rotate * this.direction);
    sketch.rect(-this.size / 2, -this.size / 2, this.size, this.size, 5);
    sketch.pop();
  }

  calcArea() {
    return this.size * this.size * this.scale;
  }
}


function createBoxes(sketch, vw, vh, clearArea, colors) {
  const boxes = [];
  const gridWidth = vw / BLOCK_COUNT_Y;
  const gridHeight = vh / BLOCK_COUNT_X;

  for (let x = 0; x <= BLOCK_COUNT_X; x++) {
    for (let y = 0; y <= BLOCK_COUNT_Y; y++) {
      const pos = sketch.createVector(
        randomBetween(gridWidth * x, gridWidth * (x + 1)),
        randomBetween(gridHeight * y, gridHeight * (y + 1))
      );

      if (clearArea.isVectorInside(pos)) {
        continue;
      }
      const box = new Box(
        pos,
        randomBetween(MAX_BLOCK_SIZE / 2, MAX_BLOCK_SIZE),
        randomItem(colors),
        randomBetween(0.5, 1),
        randomBetween(0, 1) > 0.5 ? 1 : -1,
        randomBetween(0, 2 * sketch.PI)
      );
      boxes.push(box);
    }
  }
  return boxes;
}

function createLogoArea(sketch, canvas, title, subtitle, button) {
  const canvasRect = canvas.getBoundingClientRect();
  const titleRect = title.getBoundingClientRect();
  const subtitleRect = subtitle.getBoundingClientRect();
  const buttonRect = button.getBoundingClientRect();

  const vectors = [
    sketch.createVector(titleRect.x, titleRect.y),
    sketch.createVector(titleRect.x + titleRect.width, titleRect.y),
    sketch.createVector(subtitleRect.x + subtitleRect.width, subtitleRect.y),
    sketch.createVector(subtitleRect.x + subtitleRect.width, subtitleRect.y + subtitleRect.height),
    sketch.createVector(buttonRect.x + buttonRect.width, buttonRect.y + buttonRect.height),
    sketch.createVector(buttonRect.x, buttonRect.y + buttonRect.height),
    sketch.createVector(subtitleRect.x, subtitleRect.y + subtitleRect.height),
    sketch.createVector(subtitleRect.x, subtitleRect.y),
  ];
  for (const vector of vectors) {
    // The canvas does not start from the beginning of the document.
    vector.x = vector.x - canvasRect.x;
    vector.y = vector.y  - canvasRect.y;
  }

  // Add a small margin for the entire stroke
  const minX = Math.min(...vectors.map((d) => d.x));
  const maxX = Math.max(...vectors.map((d) => d.x));
  const minY = Math.min(...vectors.map((d) => d.y));
  const maxY = Math.max(...vectors.map((d) => d.y));

  const centerX = minX + (maxX - minX) / 2;
  const centerY = minY + (maxY - minY) / 2;

  for (const vector of vectors) {
    vector.x -= centerX;
    vector.x *= 1.2;
    vector.x += centerX;
    vector.y -= centerY;
    vector.y *= 1.2;
    vector.y += centerY;
  }

  return new Polygon(sketch.createVector(0, 0), vectors);
}

export function initHeaderAnimation() {
  const canvas = document.querySelector("#header-canvas");
  const title = document.querySelector("#header-title");
  const subtitle = document.querySelector("#header-lead");
  const button = document.querySelector("#header-button");

  documentReady(function() {

    new p5((sketch) => {

      let colors = [];
      let boxes = [];
      let logoArea;
      sketch.setup = () => {
        const positionInfo = canvas.getBoundingClientRect();
        const vw = positionInfo.width; // viewport width
        const vh = positionInfo.height; // viewport height
        colors = [
          sketch.color("#017cee"),
          sketch.color("#00ad46"),
          sketch.color("#0cb6ff"),
          sketch.color("#ff7557"),
          sketch.color("#e43921"),
          sketch.color("#11e1ee"),
          sketch.color("#04d659"),
          sketch.color("#00c7d4"),
          sketch.color("#cbcbcb")
        ];
        logoArea = createLogoArea(sketch, canvas, title, subtitle, button);
        boxes = createBoxes(sketch, vw, vh, logoArea, colors);
        sketch.createCanvas(vw, vh);
      };

      sketch.draw = () => {
        sketch.background(255, 255, 255);
        if (DRAW_SAFE_AREA) {
          logoArea.draw(sketch);
        }
        boxes.forEach((box) => {
          box.calc(sketch);
          box.draw(sketch);
        });
      };

      sketch.windowResized = debounce(() => {
        const positionInfo = canvas.getBoundingClientRect();
        const vw = positionInfo.width; // viewport width
        const vh = positionInfo.height; // viewport height
        logoArea = createLogoArea(sketch, canvas, title, subtitle, button);
        boxes = createBoxes(sketch, vw, vh, logoArea, colors);
        sketch.resizeCanvas(vw, vh);
      }, 500);
    }, document.querySelector("#header-canvas"));
  });

}
