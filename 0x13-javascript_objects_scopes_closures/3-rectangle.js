#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let s = 0; s < this.height; s++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
