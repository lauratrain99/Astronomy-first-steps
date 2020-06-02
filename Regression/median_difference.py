"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020
This program calculates the median residual error of our model, i.e. 
the median difference between our predicted and actual redshifts.

"""

import numpy as np

# write a function that calculates the median of the differences
# between our predicted and actual values
def median_diff(predicted, actual):
  median_diff = np.median(abs(predicted - actual))
  return median_diff


if __name__ == "__main__":
  # load testing data
  targets = np.load('targets.npy')
  predictions = np.load('predictions.npy')

  # call your function to measure the accuracy of the predictions
  diff = median_diff(predictions, targets)

  # print the median difference
  print("Median difference: {:0.3f}".format(diff))
