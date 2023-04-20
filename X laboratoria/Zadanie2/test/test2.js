import { exists, isDirectory, isFile, readFile } from "../script.js";
import assert from 'assert';

describe('Tests for ex. 2', function () {
  it('Checks exists function', function () {
    assert.strictEqual(exists("aaa.txt"), false);
    assert.strictEqual(exists("directory"), false);
    assert.strictEqual(exists("./file.txt"), true);
    assert.strictEqual(exists("./dir"), true);
  });
  it('Checks isDirectory function', function () {
    assert.strictEqual(isDirectory("./file.txt"), false);
    assert.strictEqual(isDirectory("./dir"), true);
  });
  it('Checks isFile function', function () {
    assert.strictEqual(isFile("./file.txt"), true);
    assert.strictEqual(isFile("./dir"), false);
  });
  it('Checks readFile function', function () {
    assert.strictEqual(readFile("./file.txt"), "Should be displayed");
  });
});