class Problem:
  @property
  def definition(self):
    return 'Problem nº9: Special Pythagorean Triplet'

  @property
  def expected_sum_of_terms(self):
    return 1000

  @property
  def solved_at(self):
    return 'Problem was first solved on the 3rd of March 2024'

  def _algorithm(self, n):
    # It should be safe to assume that the largest number is n // 2
    half_of_n = n // 2
    for i in range(1, half_of_n):
      for j in range(i, half_of_n): 
        k = n - i - j
        if i**2 + j**2 == k**2:
          return i * j * k

  def solve(self):
    print(self.definition)
    return self._algorithm(self.expected_sum_of_terms)