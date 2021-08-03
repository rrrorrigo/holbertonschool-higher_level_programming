#!/usr/bin/node
const av = process.argv[2];
if (isNaN(av)) {
  console.log('Missing size');
}
for (let y = av; y > 0; y--) {
  for (let x = av; x > 0; x--) {
    process.stdout.write('X');
  }
  console.log('');
}
