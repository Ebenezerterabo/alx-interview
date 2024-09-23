#!/usr/bin/node

const request = require('request');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];
// Make a request to the star wars API to get movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // Get movie data for the given movie ID
    const movieData = JSON.parse(body);
    // Array of character URL's
    const characterUrls = movieData.characters;

    // Map over the character URL's and return an array of promises
    const characterPromises = characterUrls.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            // Resolve the promise with the character name
            resolve(JSON.parse(body).name);
          } else {
            reject(error);
          }
        });
      });
    });

    // Use Promise.all to wait for all promises to resolve
    Promise.all(characterPromises)
      .then(characters => {
        // Print each character name
        characters.forEach(character => {
          console.log(character);
        });
      })
      .catch(error => {
        console.error(error);
      });
  } else {
    console.error(error);
  }
});
