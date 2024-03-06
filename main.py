from time import time
from _10th_problem import Problem

class Main(Problem):
  def start_timer(self):
    start_time = time()
    def print_execution_time():
      execution_time = time() - start_time
      print(f'The problem took {round(execution_time * 1000, 2)} milliseconds (or {round(execution_time, 2)} seconds) to be solved')
    return print_execution_time

  def run(self):
    print(self.definition)
    end_timer = self.start_timer()
    print(f'Solution: {self.solve()}')
    end_timer()
    if self.solved_at:
      print(self.solved_at)

Main().run()