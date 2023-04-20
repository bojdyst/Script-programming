"use strict"

var expect = chai.expect;

describe('Tests', function() {
  it("cyfry", function() {
    chai.assert.equal(cyfry('321'), 6);
    chai.assert.equal(cyfry('aaa'), 0);
    chai.assert.equal(cyfry('aaa987'), 24);
    chai.assert.equal(cyfry('321aaa'), 6);
    chai.assert.equal(cyfry(''), 0);
  });

  it("litery", function() {
    chai.assert.equal(litery('123'), 0);
    chai.assert.equal(litery('aaa'), 3);
    chai.assert.equal(litery('aaa999'), 3);
    chai.assert.equal(litery('000aaa'), 3);
    chai.assert.equal(litery(''), 0);
  })

  it("suma", function() {
    total = 0;
    chai.assert.equal(suma('123'), 123);
    chai.assert.equal(suma('aaa'), 123);
    chai.assert.equal(suma('aaa321'), 123);
    chai.assert.equal(suma('321aaa'), 444);
    chai.assert.equal(suma(''), 444);
  })
});