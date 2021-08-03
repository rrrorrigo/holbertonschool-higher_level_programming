#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = this.height; h > 0; h--) {
      for (let w = this.width; w > 0; w--) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
}
module.exports = Rectangle;
