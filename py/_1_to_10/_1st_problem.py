print('Problem nº1: Multiples of 3 or 5')
print('Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.')

BASE = 1
LIMIT = 1000

list_of_multiples=[]
for index in range(BASE, LIMIT):
  is_multiple_of_five = index % 5 == 0
  is_multiple_of_three = index % 3 == 0
  if is_multiple_of_three == True or is_multiple_of_five == True:
    list_of_multiples.append(index)

sum_of_multiples = 0
for j in range(len(list_of_multiples)):
  sum_of_multiples = sum_of_multiples + list_of_multiples[j]

print('Solution:', sum_of_multiples)
# Problem was first solved on the 13th of February 2024