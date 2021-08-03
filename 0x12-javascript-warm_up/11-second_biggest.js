#!/usr/bin/node
const av = process.argv;
let r = 2;
let max = 2;
if (av.length > 3) {
  for (let index = 2; index < av.length; index++) {
    if (parseInt(av[max]) < parseInt(av[index])) {
      max = index;
    }
  }
  for (let ii = 2; ii < av.length; ii++) {
    if (parseInt(av[r]) < parseInt(av[ii]) && av[ii] !== av[max]) {
      r = ii;
    }
  }
  console.log(av[r]);
} else {
  console.log('0');
}
