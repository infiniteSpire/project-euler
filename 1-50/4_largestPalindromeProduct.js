function isNumberAPalindrome(string) {
  return string === string.split('').reverse().join('') ? string : undefined;
}

function recursiveSearchOfPalindrom(limit, base, n, palindromeNumber) {
  palindromeNumber = isNumberAPalindrome(String(base * n)) || palindromeNumber;

  if (base > limit) {
    return palindromeNumber;
  } else if (n > limit) {
    base++;
    return recursiveSearchOfPalindrom(limit, base, 900, palindromeNumber);
  } else {
    n++;
    return recursiveSearchOfPalindrom(limit, base, n, palindromeNumber);
  }
}

function largestPalindromeProduct() {
  return recursiveSearchOfPalindrom(999, 990, 900, undefined);
}

export default largestPalindromeProduct;
