#!/usr/bin/node
exports.add = function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  }
  return (parseInt(a) + parseInt(b));
};
