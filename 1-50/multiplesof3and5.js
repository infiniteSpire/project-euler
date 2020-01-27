/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

function multiplesof3and5(n) {
  const multiples = [];

  for (let i = 1; i < n; i++) {
    if (!Boolean(i % 3) || !Boolean(i % 5)) {
      multiples.push(i);
    }
  }

  return multiples;
}

function sum(numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

const result = sum(multiplesof3and5(1000));

console.log(result);
