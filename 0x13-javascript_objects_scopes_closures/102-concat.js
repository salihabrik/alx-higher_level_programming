#!/usr/bin/node
const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}
const fs = require('fs');
const content1 = fs.readFileSync(sourceFile1, 'utf8');
const content2 = fs.readFileSync(sourceFile2, 'utf8');
const concatenatedContent = content1 + content2;

fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Concatenated contents of ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
