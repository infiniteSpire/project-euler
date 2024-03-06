from helper.conditional import is_factor, is_end_of_range

def find_and_append_next_prime(primes, potential_prime):
  for prime in primes:
    if is_factor(potential_prime, prime):
      break
    if is_end_of_range(prime, primes[-1]):
      primes.append(potential_prime)
  return primes