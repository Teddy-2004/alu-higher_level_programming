#!/usr/bin/node

const input = process.argv.slice(2);

const firstArgument = input[0] !== undefined ? input[0] : "No argument";

console.log(firstArgument);
