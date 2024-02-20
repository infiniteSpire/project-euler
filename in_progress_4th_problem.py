print('Problem nº4: Largest Palindrome Product')
print('Description: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99. Find the largest palindrome made from the product of two 3-digit numbers.')

def is_palindrome(n):
  string_representation = str(n)
  first_half, second_half = string_representation[:len(string_representation)//2], string_representation[len(string_representation)//2:]
  second_half_reversed = second_half[::-1]
  return first_half == second_half_reversed

def get_largest_palindrome_of(n):
  palindromes = []
  for i in range(10, n + 1):
    for j in range(10, i + 1):
      if is_palindrome(i * j):
        palindromes.append(i)
  print('list', palindromes)

print('Solution:', get_largest_palindrome_of(40))

# IN PROGRESS