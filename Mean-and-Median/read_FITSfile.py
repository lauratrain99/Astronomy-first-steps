"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program loads in a FITS file and finds the position
of the brightest pixel (i.e. the maximum value) in its image data.
"""


# Write your load_fits function here.
from astropy.io import fits
import numpy as np

def load_fits(image):
  hdulist = fits.open(image)
  data = hdulist[0].data
  return np.unravel_index(np.argmax(data, axis=None), data.shape)


if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image0.fits')
  print(bright)

  # You can also confirm your result visually:
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.xlabel('x-pixels (RA)')
  plt.ylabel('y-pixels (Dec)')
  plt.colorbar()
  plt.show()