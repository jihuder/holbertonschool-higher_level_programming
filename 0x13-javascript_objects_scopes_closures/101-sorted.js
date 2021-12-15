#!/usr/bin/node
const dict = require('./101-data').dict;
const copy = {};
for (const key in dict) {
  if (copy[dict[key]] === undefined) {
    copy[dict[key]] = [];
  }
  copy[dict[key]].push(key);
}
console.log(copy);
