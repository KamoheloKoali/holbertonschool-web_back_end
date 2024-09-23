const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

// Read the user's input
rl.on('line', (input) => {
  console.log(`Your name is: ${input}`);
  rl.close();
});

// Print the closing message when the program ends
rl.on('close', () => {
  console.log('This important software is now closing');
  process.exit(0);
});
