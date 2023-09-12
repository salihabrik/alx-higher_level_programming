#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let s = 0; s < this.height; s++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
