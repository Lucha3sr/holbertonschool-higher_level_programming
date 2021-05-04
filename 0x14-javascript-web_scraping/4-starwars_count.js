#!/usr/bin/node
const request = require('request');
const urlId = process.argv[2] + '/?format=json';
const peopleNbr = 'https://swapi-api.hbtn.io/api/people/18/';
request.get(urlId, function (response, body) {
  const filmList = (JSON.parse(body.body).results);
  let count = 0;
  for (const film in filmList) {
    for (const chars in filmList[film].characters) {
      if (filmList[film].characters[chars] === peopleNbr) {
        count++;
      }
    }
  }
  console.log(count);
});
