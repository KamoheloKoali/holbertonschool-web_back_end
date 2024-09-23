const express = require('express');

// Créez une application Express
const app = express();

// Définissez une route pour l'endpoint /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Faites écouter le serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exportez l'application Express
module.exports = app;
