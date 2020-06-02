"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program improves the previous crossmatch.
It implements a k-d trees machine learning algorithm using the  astropy library.
It returns:
    1. A list of tuples of matched IDs and their distance in degrees.
    2. A list of unmatched IDs from the first catalogue.
    3. The time taken (in seconds) to run the crossmatcher.
"""


import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
import time

def crossmatch(cat1, cat2, max_radius):
    start = time.perf_counter()
    sky_cat1 = SkyCoord(cat1*u.degree, frame='icrs')
    sky_cat2 = SkyCoord(cat2*u.degree, frame='icrs')
    closest_ids, closest_dists, closest_dists3d = sky_cat1.match_to_catalog_sky(sky_cat2)
    closest_dists_array = closest_dists.value
    matches = []
    no_matches = []
    point = 1
    for id1, (closest_id2, distance) in enumerate(zip(closest_ids, closest_dists_array)):
        if distance < max_radius:
            matches.append((id1, closest_id2, distance))
        else:
            no_matches.append(id1)
    
    total_time = time.perf_counter() - start
    return matches, no_matches, total_time

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