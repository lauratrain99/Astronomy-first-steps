"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program times our different statistical implementations.
"""


import numpy as np
import statistics
import time


def time_stat(func, size, ntrials):
  total = 0
  data = np.random.rand(size)
  for i in range(ntrials):
    start = time.perf_counter()
    res = func(data)
    end = time.perf_counter() - start
    total += end
  # return the average run time
  return total/ntrials

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))