#!/usr/bin/node
/* Class Rectangle */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print a rectangle
  print () {
    let line;
    for (let i = 0; i < this.height; i++) {
      line = 'X';
      for (let j = 0; j < this.width - 1; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  // Method that exchanges the width and the height
  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  // Method that multiples the width and the height
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
