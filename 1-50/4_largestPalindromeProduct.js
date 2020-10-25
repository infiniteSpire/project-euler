function getPalindromeNumber(string) {
  return string === string.split('').reverse().join('') ? string : undefined;
}

function recursivelyReduceNumber(number) {
  const palindromeNumber = getPalindromeNumber(String(number * (number + 1))) || getPalindromeNumber(String(number * number));
  return palindromeNumber || recursivelyReduceNumber(number - 1);
}

function largestPalindromeProduct() {
  return recursivelyReduceNumber(100);
}

export default largestPalindromeProduct;
