const countStudents = require('./2-read_file');

countStudents('nope.csv');
throw new Error('Cannot load the database');
