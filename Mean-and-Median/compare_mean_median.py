"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program takes a list of numbers and returns 
a tuple of the median and mean of the list (in this order).
"""

# Write your function median_FITS here:
def list_stats(list_numbers):
  list_numbers.sort()
  mean = sum(list_numbers)/len(list_numbers)
  if len(list_numbers) % 2 != 0:
    mid = len(list_numbers)//2
    median = list_numbers[mid]
  else:
    mid = len(list_numbers)//2
    median = (list_numbers[mid-1] + list_numbers[mid])/2
  return median,mean

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
print(list_stats([1.3, 2.4, 20.6, 0.95, 3.1]))
print(list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7]))
print(list_stats([1.5]))