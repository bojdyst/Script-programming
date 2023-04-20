import * as fs from 'node:fs';

if (process.argv[2] != null)
{
    var path = process.argv[2];

    if (exists(path)) {
        console.log("Path exists");
    } else {
        console.log("Path DOESN'T exists");
    }

    if (isDirectory(path)) {
    }

    if (isFile(path)) {
        console.log(path + " is a file and its content is:\n" + readFile(path));
    }
}

export function exists(path) {
    if (fs.existsSync(path)) {
        return true;
    } else {
        return false;
    }
}

export function isFile(path) {
    if (exists(path) && fs.statSync(path).isFile()) {
        return true;
    } else {
        return false;
    }
}

export function isDirectory(path) {
    if (exists(path) && fs.statSync(path).isDirectory()) {
        return true;
    } else {
        return false;
    }
}

export function readFile(path) {
    var data = fs.readFileSync(path,
        {encoding:"utf8", flag:"r"});
    return data;
}