"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program improves the previous crossmatch.
It breaks out of the loop over the second catalogue
when the declination reaches dec1 + max_radius.
It returns:
    1. A list of tuples of matched IDs and their distance in degrees.
    2. A list of unmatched IDs from the first catalogue.
    3. The time taken (in seconds) to run the crossmatcher.
"""


# Write your crossmatch function here.
import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return  np.degrees(2*np.arcsin(np.sqrt(a + b)))


def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  matches = []
  no_matches = []
  
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  sort_ind = np.argsort(cat2[:,1])
  cat2 = cat2[sort_ind]
  
  for point in range(cat1.shape[0]):
      ra1 = cat1[point,0]
      dec1 = cat1[point,1]

      distances = []
      for i in range(len(cat2)):
          ra2 = cat2[i,0]
          dec2 = cat2[i,1]
          if dec2 >= dec1 + max_radius:
              break
          distances.append(angular_dist(ra1,dec1,ra2,dec2))
      distances = np.array(distances)
      
      arg_closest_distance = np.argmin(distances)
      closest_distance = np.amin(distances)
      

      if closest_distance < max_radius:
        matches.append((point, sort_ind[arg_closest_distance], closest_distance))
      else:
        no_matches.append(point)
      
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