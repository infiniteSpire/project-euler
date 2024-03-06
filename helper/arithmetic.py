from functools import reduce

def get_next_uneven_number(n):
  return n + 2

def get_sum_of(numbers):
  return reduce(lambda a, b: a + b, numbers)