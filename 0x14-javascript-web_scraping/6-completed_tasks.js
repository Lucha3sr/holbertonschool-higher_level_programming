#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (response, body) {
  const tasks = (JSON.parse(body.body));
  const tasksDone = {};
  let count = 0;
  for (const task in tasks) {
    const userID = tasks[task].userId;
    if (!(userID in tasksDone)) {
      count = 0;
    }
    if (tasks[task].completed === true) {
      count++;
    }
    tasksDone[userID] = count;
  }
  console.log(tasksDone);
});
