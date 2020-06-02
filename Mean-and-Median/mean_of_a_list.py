"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This programs computes the mean of a list. The output is a scalar.
"""

# Write your calculate_mean function here.
def calculate_mean(list):
  return sum(list)/len(list)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calculate_mean` function with examples:
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
