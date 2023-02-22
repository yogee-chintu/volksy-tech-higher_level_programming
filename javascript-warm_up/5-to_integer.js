#!/usr/bin/node
if (isNan(parseInt(process.argv[2], 10))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2], 10));
