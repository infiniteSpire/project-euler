function largestPrimeFactor() {
  const getPrimeFactors = function(number) {
    let primeFactors = [];

    for (let i = 2; i <= number; i++) {
      if (number % i === 0) {
        primeFactors.push(i);
        number = number / i;
        i = 2;
      }
    }

    return primeFactors;
  };

  return Math.max(...getPrimeFactors(600851475143));
}

export default largestPrimeFactor;
