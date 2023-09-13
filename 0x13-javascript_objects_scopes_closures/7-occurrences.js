#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbOccurence = 0;
  for (let s = 0; s < list.length; s++) {
    if (list[s] === searchElement) {
      nbOccurence++;
    }
  }
  return nbOccurence;
};
