function smallestMultiple(number = 1) {
  while (true) {
    for (let i = 1; i <= 20; i++) {
      if (number % i === 0) {
        if (i === 20) {
          return number;
        }

        continue;
      }

      break;
    }

    number++;
  }
}

export default smallestMultiple;
