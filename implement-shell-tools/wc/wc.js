const fs = require("fs");

const args = process.argv.slice(2);

let showWords = false;
let showChars = false;
let showLines = false;
let fileNames = [];

// Check flags and file names
for (let item of args) {
    if (item === "-l") {
        showLines = true;
    } else if (item === "-w") {
        showWords = true;
    } else if (item === "-c") {
        showChars = true;
    } else {
        fileNames.push(item);
    }
}

// If no flags are given, show everything
if (!showLines && !showWords && !showChars) {
    showLines = true;
    showWords = true;
    showChars = true;
}

for (let fileName of fileNames) {
    let text = fs.readFileSync(fileName, "utf8");

    let totalLines = text.split("\n").length - 1;
    let totalWords = text.trim().split(/\s+/).length;
    let totalChars = Buffer.byteLength(text);

    let output = "";

    if (showLines) output += totalLines + " ";
    if (showWords) output += totalWords + " ";
    if (showChars) output += totalChars + " ";

    output += fileName;

    console.log(output);
}