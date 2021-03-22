#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
if ( isNaN(firstArg) === false) {
  let i;
  let ii;
  for (i = 0; i < firstArg; i++) {
    for (ii = 0; ii < firstArg; ii++) {
      process.stdout.write('X');
    }
    console.log(' ');
  }
} else {
  console.log('Missing size');
}
