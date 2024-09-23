const express = require('express');

const app = express();
const port = 1245;

// Обработчик для корневого маршрута
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Обработка ошибок 404
app.use((req, res) => {
  res.status(404).send('Not Found');
});

// Запуск сервера
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

module.exports = app;
