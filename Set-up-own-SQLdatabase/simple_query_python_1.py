"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

Replicate the following query in Python:
SELECT kepler_id, radius
FROM Star
WHERE radius > 1.0;
"""

# Write your query function here
import numpy as np
def query(cvs_filename):
  data = np.loadtxt(cvs_filename, delimiter = ',', usecols = (0,2))
  data = data[data[:,1] > 1]
  return data


# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print(result)