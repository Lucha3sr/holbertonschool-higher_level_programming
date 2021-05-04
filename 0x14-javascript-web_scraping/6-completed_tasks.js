#!/usr/bin/node
let request = require('request');
request(process.argv[2], function (response, body) {
  let tasks = (JSON.parse(body.body));
  let tasksDone = {};
  let count = 0;
  for (let task in tasks) {
    let userID = tasks[task].userId;
    if (!(userID in tasksDone)) {
      count = 0;
    }
    if (tasks[task].completed) {
      count += 1;
    }
    tasksDone[userID] = count;
  }
  console.log(tasksDone);
});
