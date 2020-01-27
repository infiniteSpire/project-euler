function multiplesof3and5() {

  const filterMultiples = function(n) {
    const multiples = [];

    for (let i = 1; i < n; i++) {
      if (!Boolean(i % 3) || !Boolean(i % 5)) {
        multiples.push(i);
      }
    }

    return multiples;
  };

  const sum = function(numbers) {
    return numbers.reduce((a, b) => a + b, 0);
  };

  return sum(filterMultiples(1000));
}

export default multiplesof3and5;
