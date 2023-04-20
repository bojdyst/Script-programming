//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8000");

// UNIT test begin
describe('Tests for ex.3', function () {
      it('checks non-existing path provided', function (done) {
            server
                  .get('/submit?path=aaaaa')
                  .expect('Content-Type', /text\/plain/)
                  .expect(200, "Path doesn't exist.", done);
      });

      it('checks existing file provided', function (done) {
            server
                  .get('/submit?path=file.txt')
                  .expect('Content-Type', /text\/plain/)
                  .expect(200, "file.txt is a file with content: Should be displayed", done);
      });

      it('checks existing directory provided', function (done) {
            server
                  .get('/submit?path=test')
                  .expect('Content-Type', /text\/plain/)
                  .expect(200, "test is a directory.", done);
      });
});