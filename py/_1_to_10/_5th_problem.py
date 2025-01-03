print('Problem nº5: Smallest Multiple')
print('Description: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?')

def is_factor(n, o):
  return n % o == 0

def get_smallest_multiple(start_index, end_index):
  factor = end_index
  smallest_multiple_in_common = 0
  while smallest_multiple_in_common == 0:
    product = end_index * factor
    for i in range(end_index - 1, start_index - 1, -1):
      if is_factor(product, i) == False:
        break
      if i == start_index:
        smallest_multiple_in_common = product
    factor += 1
  return smallest_multiple_in_common

print('Solution:', get_smallest_multiple(1, 20))
# Problem was first solved on the 26th of February 2024