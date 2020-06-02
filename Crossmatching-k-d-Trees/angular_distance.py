"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program computes the angular distance between any two points 
on the celestial sphere given their right ascension and declination. 
"""


# Write your angular_dist function here.
import numpy as np
def angular_dist(r1, d1, r2, d2):
  r1 = np.radians(r1)
  r2 = np.radians(r2)
  d1 = np.radians(d1)
  d2 = np.radians(d2)
  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return  np.degrees(2*np.arcsin(np.sqrt(a + b)))

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))
