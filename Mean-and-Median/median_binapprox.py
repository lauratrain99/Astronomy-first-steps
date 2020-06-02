"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program implements the binapprox algorithm
to calculate the median of a list of numbers.
"""

# Import the running_stats function
import numpy as np

# Write your median_bins_fits and median_approx_fits here:
def median_bins(list_values,nBins):
  values = np.array(list_values)
  mean = np.mean(values)
  std = np.std(values)
  bin_ignore = np.count_nonzero(values < mean-std)
  
  width = 2*std/nBins
  minval = mean - std
  bincounts = []
  for i in range(nBins):
    bincounts.append(values[(minval + width*i <= values) & (values < minval + width*(i+1))].size)
  return (mean, std, bin_ignore, np.array(bincounts))

def median_approx(list_values,nBins):
  values = np.array(list_values)
  mean, std, bin_ignore, bincounts = median_bins(list_values,nBins)
  N = len(list_values)
  width = 2*std/nBins
  minval = mean - std
  sum_counts = bin_ignore
  N = len(values)
  mid = (N + 1)/2
  
  for ind,bin in enumerate(bincounts):
    sum_counts += bin
    if sum_counts >= mid:
       break
  return minval + width*ind + width/2

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1,1,3,2,2,6], 3))
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_bins([0, 1], 5))
  print(median_approx([0, 1], 5))