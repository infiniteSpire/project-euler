print('Problem nº3: Largest Prime Factor')
print('Description: The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?')

SMALLEST_PRIME = 2

def is_factor(n, o):
  return n % o == 0

def is_prime(n):
  if (n < SMALLEST_PRIME):
    return False

  for i in range(SMALLEST_PRIME, n):
    if is_factor(n, i):
      return False
  return True

def get_largest_prime_factor_of(n):
  largest_prime_factor = SMALLEST_PRIME
  for i in range(SMALLEST_PRIME, n):
    if is_factor(n, i) and is_prime(i):
      largest_prime_factor = i
  return largest_prime_factor

print('Solution:', get_largest_prime_factor_of(13195))