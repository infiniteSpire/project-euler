from time import time

print('Problem nº7: 10001st Prime')
print('Description: By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.')

def is_factor(n, o):
  return n % o == 0

def is_end_of_range(n, o):
  return n == o

def get_next_uneven_number(n):
  return n + 2

def get_nth_prime(n):
  primes = [2]
  potential_prime = 3
  while len(primes) < n:
    for prime in primes:
      if is_factor(potential_prime, prime):
        break
      if is_end_of_range(prime, primes[-1]):
        primes.append(potential_prime)
    potential_prime = get_next_uneven_number(potential_prime)
  return primes[-1]

start_time = time()

print('Solution:', get_nth_prime(10001))

end_time = time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")