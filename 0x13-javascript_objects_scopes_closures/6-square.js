#!/usr/bin/node
const Rectangle = require("./4-rectangle");
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let h = this.height; h > 0; h--) {
      for (let w = this.width; w > 0; w--) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}
module.exports = Square;
