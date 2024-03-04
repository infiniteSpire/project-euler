from time import time
from _9th_problem import Problem

class Main(Problem):
  def start_timer(self):
    start_time = time()
    def print_execution_time():
      # trunc the decimal part. Are those actually seconds?
      print(f'The problem took {time() - start_time} seconds to be solved')
    return print_execution_time

  def run(self):
    end_timer = self.start_timer()
    solution = self.solve()
    print(f'Solution: {solution}')
    end_timer()

Main().run()
