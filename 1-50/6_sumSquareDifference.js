function sumSquareDifference() {
  const limit = 100;
  let squareOfSum = 0;
  let sumOfSquares = 0;

  for (let i = 1; i <= limit; i++) {
    squareOfSum += i;
    sumOfSquares += i**2;
  }

  squareOfSum = squareOfSum**2;

  return squareOfSum - sumOfSquares;
}

export default sumSquareDifference;
