#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

    print() {
    let i;
    let ii;
    for (i = 0; i < this.height; i++) {
      for (ii = 0; ii < this.width; ii++) {
	  process.stdout.write('X');
      }
      console.log();
    }
    }
};
