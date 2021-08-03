#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  }
  return (parseInt(a) + parseInt(b));
}
const av = process.argv;
console.log(add(av[2], av[3]));
