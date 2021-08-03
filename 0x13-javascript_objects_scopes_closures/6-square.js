#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
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
