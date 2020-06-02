"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program vectorises the previous crossmatch.
It uses a for loop in the angular distance function.
It returns:
    1. A list of tuples of matched IDs and their distance in degrees.
    2. A list of unmatched IDs from the first catalogue.
    3. The time taken (in seconds) to run the crossmatcher.
"""


# Write your crossmatch function here.
import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
  dists = np.zeros((len(r2),))
  for i in range(len(r2)):
    a = np.sin(np.abs(d1-d2[i])/2)**2
    b = np.cos(d1)*np.cos(d2[i])*np.sin(np.abs(r1 - r2[i])/2)**2
    dists[i] = (2*np.arcsin(np.sqrt(a + b)))
  return  dists

def find_closest(cat, ra1, dec1):
  ra2s = cat[:, 0]
  dec2s = cat[:, 1]
  dists = angular_dist(ra1, dec1, ra2s, dec2s)
  return np.argmin(dists), np.amin(dists)


def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  matches = []
  no_matches = []
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  max_radius = np.radians(max_radius)
  for point in range(len(cat1)):
      closest_distance = find_closest(cat2, cat1[point,0], cat1[point,1])
      if closest_distance[1] < max_radius:
        matches.append((point, closest_distance[0], np.degrees(closest_distance[1])))
      else:
        no_matches.append(point)
  total_time = time.perf_counter() - start
  return matches, no_matches, total_time

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  ra1, dec1 = np.radians([180, 30])
  cat2 = [[180, 32], [55, 10], [302, -44]]
  cat2 = np.radians(cat2)
  ra2s, dec2s = cat2[:,0], cat2[:,1]
  dists = angular_dist(ra1, dec1, ra2s, dec2s)
  print(np.degrees(dists))

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