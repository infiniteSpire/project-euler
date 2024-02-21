function isPrime(int) {
  if (int === 2 || int % 2) {
    for (let i = 2; i < int; i++) {
      if (int % i === 0) {
        return false;
      }
    }

    return true;
  }

  return false;
}

function prime10001st() {
  let index = 2;
  let counter = 0;
  const limit = 10001;

  while(true) {
    if (isPrime(index)) {
      counter++;

      if (counter === 10001) {
        break;
      }
    }

    index++;
  }

  return index;
}

export default prime10001st;
