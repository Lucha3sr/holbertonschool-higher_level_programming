#!/usr/bin/node
let args = process.argv.splice(0,2);
args = args.sort;
if (args.length <= 0){
console.log(0);
}
let i;
let ii;
for (i = 0; i < args; i++) {
    for (ii = 0; ii < args; ii++) {
	if (args[i] < args[ii]){
	    console.log(args[i]);
	}
    }
}
