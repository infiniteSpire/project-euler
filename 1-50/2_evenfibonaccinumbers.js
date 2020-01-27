function evenfibonaccinumbers() {
  const fibonacciNumbers = function(numbers) {
    while(numbers[numbers.length - 1] < 4000000) {
      const nextNumberInSequence = numbers[numbers.length - 1] + numbers[numbers.length - 2];

      if (nextNumberInSequence > 4000000) {
        break;
      }

      numbers.push(nextNumberInSequence);
    }

    return numbers;
  };

  const sumEvenNumbers = function(sequence) {
    return sequence.filter(number => !Boolean(number % 2)).reduce((a, b) => a + b, 0);
  };

  return sumEvenNumbers(fibonacciNumbers([0, 1]));
}

export default evenfibonaccinumbers;
