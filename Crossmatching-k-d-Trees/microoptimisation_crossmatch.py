"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program is a microoptimisation of the previous crossmatch.
It converts all the coordinates to radians before it starts crossmatching.
It returns:
    1. A list of tuples of matched IDs and their distance in degrees.
    2. A list of unmatched IDs from the first catalogue.
    3. The time taken (in seconds) to run the crossmatcher.
"""

import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return  np.degrees(2*np.arcsin(np.sqrt(a + b)))

def find_closest(cat, r, d):
  distances = []
  for i in range(len(cat)):
    distances.append(angular_dist(r,d,cat[i][0],cat[i][1]))
  distances = np.array(distances)
  return np.argmin(distances), np.amin(distances)


def crossmatch(cat1, cat2, max_radius):
  start_time = time.clock()
  matches = []
  no_matches = []
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  for point in range(len(cat1)):
      closest_distance = find_closest(cat2, cat1[point][0], cat1[point][1])
      if closest_distance[1] < max_radius:
        matches.append((point, closest_distance[0], closest_distance[1]))
      else:
        no_matches.append(point)
  end_time = time.clock()
  return matches, no_matches, (end_time-start_time)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))
  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)