#!/usr/bin/node
const av = process.argv;
let i = av[2];
if (isNaN(i)) {
  console.log('Missing number of occurrences');
}
for (i = av[2]; i > 0; i--) {
  console.log('C is fun');
}
