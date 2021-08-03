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

  rotate () {
    this.height = this.height + this.width;
    this.width = this.height - this.width;
    this.height = this.height - this.width;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
