from math import sqrt
from _1_to_10.helper.conditional import is_factor

def find_and_append_next_prime(primes, potential_prime):
  for prime in primes:
    if is_factor(potential_prime, prime):
      break
    if prime > sqrt(potential_prime):
      primes.append(potential_prime)
      break
  return primes

"""
  Why prime > sqrt(potential_prime) is enough to check if potential_prime is prime?
    When checking if a number n is prime, we don't actually need to check all numbers
    less than n to see if they are factors of n. We only need to check numbers up to
    the square root of n. Here's why: If n is not a prime number, then it can be
    factored into two factors, a and b (i.e., n = a * b). If both a and b were greater
    than the square root of n, then a * b would be greater than n, which is not possible.
    Similarly, if both a and b were less than the square root of n, then a * b would be
    less than n, which is also not possible. Therefore, at least one of a or b must be
    less than or equal to the square root of n.
"""