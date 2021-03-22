#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) === true) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }
  return (n * factorial(n - 1));
}
const firstArg = parseInt(process.argv[2]);
console.log(factorial(firstArg));
