"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

Replicate the following query in Python:
SELECT p.radius/s.radius AS radius_ratio
FROM Planet AS p
INNER JOIN star AS s USING (kepler_id)
WHERE s.radius > 1.0
ORDER BY p.radius/s.radius ASC;
"""


# Write your query function here
import numpy as np

def query(fname_1, fname_2):
  stars = np.loadtxt(fname_1, delimiter=',', usecols=(0, 2))
  planets = np.loadtxt(fname_2, delimiter=',', usecols=(0, 5))

  f_stars = stars[stars[:,1]>1, :]                
  s_stars = f_stars[np.argsort(f_stars[:, 1]), :] 
 
  final = np.zeros((1, 1))
  for i in range(s_stars.shape[0]):
    kep_id = s_stars[i, 0]
    s_radius = s_stars[i, 1]

    matching_planets = planets[np.where(planets[:, 0] == kep_id), 1].T
    final = np.concatenate((final, matching_planets/s_radius))

  return np.sort(final[1:], axis = 0)
    


# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
  print(result)