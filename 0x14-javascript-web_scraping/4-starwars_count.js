#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter((film) => film.characters.includes(characterId)).length;
    console.log(count);
  } else {
    console.error(error);
  }
});
