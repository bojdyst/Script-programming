//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

// UNIT test begin
describe('GET /', function () {
  it('Response validation', function (done) {
    server
      .get('/')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });
})

describe('JSON test', function () {	
      it('Output validation', function (done) {
        expect('./ops.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 1,
          "op": "+",
          "y": 23
        })
        expect('./ops.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 21,
          "op": "-",
          "y": 1
        })
        expect('./ops.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 6,
          "op": "*",
          "y": 5
        })
        expect('./ops.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 666,
          "op": "/",
          "y": 6
        })
        done()
      })
})

describe('GET /json/:name', function () {
      it('Response validation', function (done) {
        server
          .get('/json/ops.json')
          .expect('Content-Type', /html/)
          .expect(200, done);
      });
})

describe('GET /calculate/:operation/:x/:y', function () {
  it('Response validation', function (done) {
    server
      .get('/calculate/+/15/15')
      .expect('Content-Type', /html/)
      .expect(200, done);
  })
})

describe('GET /results', function () {
  it('Response validation', function (done) {
    server
      .get('/results')
      .expect('Content-Type', /html/)
      .expect(200, done);
  })
})
