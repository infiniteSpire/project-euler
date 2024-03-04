print('Problem nº3: Largest Prime Factor')
print('Description: The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?')

SMALLEST_PRIME = 2

def is_factor(n, o):
  return n % o == 0

def get_largest_prime_factor(n):
  i = SMALLEST_PRIME
  # as long as the factor is inferior to the simplified number, try to factorize it further
  while i < n:
    if is_factor(n, i):
      # if n has a factor, n is not a prime
      n //= i
    else:
      # if not divisible by current factor, increment factor and try again
      i += 1

  return n

print('Solution:', get_largest_prime_factor(600851475143))
# Problem was first solved on the 21st of February 2024