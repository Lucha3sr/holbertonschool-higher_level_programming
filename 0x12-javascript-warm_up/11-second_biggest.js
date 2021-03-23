#!/usr/bin/node
let args = process.argv.splice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args = args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
