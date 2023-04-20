import { Operation } from "./module.js";

const obj = new Operation(parseInt(process.argv[2]), parseInt(process.argv[3]));
console.log(obj.sum());



// const imp = require('./module');

// let obj = new imp.Operation(1,1)

// console.log(obj.sum());

