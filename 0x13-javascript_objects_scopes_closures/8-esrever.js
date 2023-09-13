#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  for (let s = list.length - 1; s >= 0; s--) {
    reversedList.push(list[s]);
  }

  return reversedList;
};
