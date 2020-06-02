"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program computes the mean of a 1D NumPy array. The output is a scalar.
"""


# Write your calc_stats function here.

import numpy as np
def calc_stats(file):
  data = np.loadtxt(file,delimiter=',')
  return round((np.mean(data)), 1),round((np.median(data)), 1)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data4.csv')
  print(mean)
 