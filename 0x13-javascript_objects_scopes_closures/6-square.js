#!/usr/bin/node
const PrevSquare = require('./5-square');
module.exports = class Square extends PrevSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let ii = 0; ii < this.width; ii++) {
          process.stdout.write(`${c}`);
        }
        console.log();
      }
    } else {
      super.print();
    }
  }
};
