#!/usr/bin/node
const av = process.argv;
const fd = require('fs');
if (av.length > 4) {
  fd.readFile(av[2], 'utf-8', function (err, data) {
    if (!err) {
      fd.readFile(av[3], 'utf-8', function (err, data2) {
        if (!err) {
          const s = data + '\n' + data2;
          fd.writeFile(av[4], s, function () {});
        }
      });
    }
  });
}
