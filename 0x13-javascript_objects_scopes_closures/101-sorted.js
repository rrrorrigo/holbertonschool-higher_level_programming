#!/usr/bin/node
const d = require('./101-data').dict;
const sorted = [];
const tempDict = {};
const key = Object.keys(d);
for (const key in d) {
  sorted[sorted.length] = d[key];
}
sorted.sort();
for (let i = 0; i < sorted.length; i++) {
  tempDict[sorted[i]] = key.map(function (k) {
    if (sorted[i] === d[k]) {
      return k;
    }
    return undefined;
  }).filter(item => item);
}
console.log(tempDict);
