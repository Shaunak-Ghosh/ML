let node = require("node");
let npm = require("npm");
let runkitnpm = require("runkit");
let repl = require("repl");

console.log("Installing chai and mocha");

var answer = prompt("Would you like to install npm packages");

if (answer == "yes") {
  console.log("running npm install --save-dev chai in hacker-code237/ml/core/core.js")
  var chai = require('chai');  
  var assert = chai.assert;
  var expect = chai.expect;
  var should = chai.should();
  console.log("running npm i mocha in hacker-code237/ml/core/core.js")
  var mocha = require("mocha")
} else if (answer == "no") {
  alert("OK, continuing without npm")
  console.error(obj1 [, obj2, ..., objN]);
  console.error(msg [, subst1, ..., substN]);
} else {
  alert("Unknown")
};
