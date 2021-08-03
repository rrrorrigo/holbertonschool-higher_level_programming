#!/usr/bin/node
exports.esrever = function (list) {
  const listreverse = [];
  for (let l = list.length - 1; l >= 0; l--) {
    listreverse.push(list[l]);
  }
  return (listreverse);
};
