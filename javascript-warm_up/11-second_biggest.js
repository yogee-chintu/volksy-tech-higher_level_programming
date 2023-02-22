#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let largest, second;
  if (parseInt(process.argv[2]) >= parseInt(process.argv[3])) {
    largest = parseInt(process.argv[2]);
    second = parseInt(process.argv[3]);
  } else {
    largest = parseInt(process.argv[3]);
    second = parseInt(process.argv[2]);
  }
