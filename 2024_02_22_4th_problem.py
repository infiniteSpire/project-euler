import math

print('Problem nº4: Largest Palindrome Product')
print('Description: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99. Find the largest palindrome made from the product of two 3-digit numbers.')

SMALLEST_THREE_DIGIT_NUMBER = 100

def is_even(str):
  return len(str) % 2 == 0

def is_palindrome(n):
  if n < 10:
    return False

  n_in_string = str(n)
  half_of_length = len(n_in_string)//2
  uneven_offset = 0 if is_even(n_in_string) else 1
  first_half_of_number = n_in_string[:math.trunc(half_of_length) + uneven_offset]
  second_half_of_number = n_in_string[math.trunc(half_of_length):]
  second_half_of_number_reversed = second_half_of_number[::-1]
  return first_half_of_number == second_half_of_number_reversed

def can_product_be_higher_than_palindrome(product, palindrome):
  return product < palindrome

def get_largest_palindrome_of(n):
  largest_palindrome = 1001

  for i in range(n, SMALLEST_THREE_DIGIT_NUMBER, -1):
    if can_product_be_higher_than_palindrome(i * i, largest_palindrome):
      break
    for j in range(i, SMALLEST_THREE_DIGIT_NUMBER, -1):
      product = i * j
      if can_product_be_higher_than_palindrome(product, largest_palindrome):
        break
      if is_palindrome(product):
        largest_palindrome = product if product > largest_palindrome else largest_palindrome
        break

  return largest_palindrome

print('Solution:', get_largest_palindrome_of(999))