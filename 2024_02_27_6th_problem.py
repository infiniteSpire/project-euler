from math import pow
from functools import reduce

print('Problem nº6: Sum Square Difference')
print('Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.')

def get_square_of_sums(numbers):
  sum_of_numbers = reduce(lambda a, b: a + b, numbers)
  return pow(sum_of_numbers, 2)

def get_sum_of_squares(numbers):
  # This reduce function assumes that the first number is 1, its square is omitted since it would be 1 anyway
  sum_of_squares = reduce(lambda a, b: a + pow(b, 2), numbers)
  return sum_of_squares

def get_difference(start_number, end_number):
  numbers = list(range(start_number, end_number + 1))
  return get_square_of_sums(numbers) - get_sum_of_squares(numbers)

print('Solution:', get_difference(1, 100))