#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const retDict = {};
request(url, function (error, response, body) {
  if (error) throw error;
  const res = JSON.parse(body);
  for (let i = 0; i < res.length; i++) {
    if (res[i].completed === true) {
      if (res[i].userId in retDict) retDict[res[i].userId] += 1;
      else retDict[res[i].userId] = 1;
    }
  }
  console.log(retDict);
});
