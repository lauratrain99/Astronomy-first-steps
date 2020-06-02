"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program imports the AT20G BSS and SuperCOSMOS catalogues
from the files bss.dat and super.csv.
It returns a list of tuples containing the object's ID (an integer)
and the coordinates in degrees
"""

# Write your import_bss function here.
import numpy as np
def hms2dec(hours, mins, seconds):
  return 15*(hours + mins/60 + seconds/(60*60))

def dms2dec(degrees, arcmin, arcsec):
  return degrees + arcmin/60 + arcsec/(60*60) if degrees > 0 else -1*(-degrees + arcmin/60 + arcsec/(60*60))

def import_bss():
  new_set = []
  data = np.loadtxt('bss.dat', usecols=range(1, 7))
  for i in range(data.shape[0]):
    decimalRA = hms2dec(data[i,0], data[i,1], data[i,2])
    decimalD = dms2dec(data[i,3], data[i,4], data[i,5])
    new_set.append((i+1, decimalRA, decimalD))
  return new_set

def import_super():
  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  data_set = []
  for i in range(data.shape[0]):
    data_set.append((i+1,data[i,0],data[i,1]))
  return data_set


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)