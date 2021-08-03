#!/usr/bin/node
function fac (n) {
  if (n > 1) {
    return (n * fac(n - 1));
  }
  return (1);
}
const av = process.argv[2];
console.log(fac(av));
