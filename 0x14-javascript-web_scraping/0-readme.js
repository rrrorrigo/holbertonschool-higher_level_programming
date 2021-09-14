#!/usr/bin/node
const av = process.argv[2];
const fs = require('fs');
fs.readFile(av, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
