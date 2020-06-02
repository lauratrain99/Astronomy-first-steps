"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program  takes a list of FITS filenames, 
loads them into a NumPy array, and calculates the median image.
It returns return a tuple of the median NumPy array, 
the time it took the function to run, and the amount of memory (in kB)
used to store all the FITS files in the NumPy array in memory.
"""


# Write your function median_FITS here:
import numpy as np
from astropy.io import fits
import time

def median_fits(list_images):
  start = time.perf_counter()
  data = []
  for image in list_images:
    hdulist = fits.open(image)
    data.append(hdulist[0].data)
    hdulist.close()
  data_stack = np.dstack(data)
  end = time.perf_counter() - start
  memory = data_stack.nbytes/ 1024
  return np.median(data_stack,axis = 2), end, memory


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(4)])
  print(result[0][100, 100], result[1], result[2])