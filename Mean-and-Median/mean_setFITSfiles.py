"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program takes a list of FITS files as an argument, 
reads them in, and returns the mean image data of the FITS files.
"""


# Write your mean_fits function here:
from astropy.io import fits

def mean_fits(list_images):
  hdulist = fits.open(list_images[0])
  data = hdulist[0].data
  hdulist.close()
  
  for i in range(1,len(list_images)):
    hdulist = fits.open(list_images[i])
    data += hdulist[0].data
    hdulist.close()
  return data/len(list_images)



if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])
  print(data[100,100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()