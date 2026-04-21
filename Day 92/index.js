console.log("12oo");
import fs from 'fs';
fs.mkdir("./lomi", () => {})


const myPackageFile = 

{
  "name": "day-92",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "node index.js"
  },
  "type": "module"
  
}








;


fs.writeFile("./lomi/package.json", JSON.stringify(myPackageFile, null, 2), () => {})