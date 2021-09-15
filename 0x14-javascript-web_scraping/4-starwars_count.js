#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, res, body) {
  if (error) throw error;
  const response = JSON.parse(body).results;
  let cant = 0;
  for (const film in response) {
    const character = response[film].characters;
    for (const charac in character) {
      if (character[charac].includes('18')) cant++;
    }
  }
  console.log(cant);
});
