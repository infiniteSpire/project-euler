from _1_to_10.algorithm.trial_division import find_and_append_next_prime
from _1_to_10.helper.arithmetic import get_next_uneven_number, get_sum_of

class Problem:
  @property
  def definition(self):
    return 'Problem nº10: Summation of Primes'

  @property
  def threshold_number(self):
    return 2000000

  @property
  def solved_at(self):
    return 'Problem was first solved on the 6th of March 2024'

  def _algorithm(self):
    primes = [2]
    potential_prime = 3
    while primes[-1] < self.threshold_number:
      primes = find_and_append_next_prime(primes, potential_prime)
      potential_prime = get_next_uneven_number(potential_prime)
    return get_sum_of(primes[:-1])

  def solve(self):
    return self._algorithm()