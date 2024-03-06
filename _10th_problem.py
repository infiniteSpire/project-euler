from algorithm.prime import find_and_append_next_prime
from helper.arithmetic import get_next_uneven_number, get_sum_of

class Problem:
  @property
  def definition(self):
    return 'Problem nº10: '

  @property
  def threshold_number(self):
    return 200000

  @property
  def solved_at(self):
    return ''

  def _algorithm(self):
    primes = [2]
    potential_prime = 3
    while primes[-1] < self.threshold_number:
      primes = find_and_append_next_prime(primes, potential_prime)
      potential_prime = get_next_uneven_number(potential_prime)
    return get_sum_of(primes[:-1])

  def solve(self):
    return self._algorithm()
  
# TODO While the algorithm is correct, it is not efficient enough to solve the problem in a reasonable time.