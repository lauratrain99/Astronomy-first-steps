"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program takes a catalogue and the position of a target source 
(a right ascension and declination) and finds the closest match 
for the target source in the catalogue.
It returns the ID of the closest object and the distance to that object.
"""

# Write your find_closest function here
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

def angular_dist(r1, d1, r2, d2):
  r1 = np.radians(r1)
  r2 = np.radians(r2)
  d1 = np.radians(d1)
  d2 = np.radians(d2)
  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return  np.degrees(2*np.arcsin(np.sqrt(a + b)))

def find_closest(cat, r, d):
  distances = []
  for i in range(len(cat)):
    distances.append(angular_dist(r,d,cat[i][1],cat[i][2]))
  distances = np.array(distances)
  return np.argmin(distances) + 1,np.amin(distances)
  

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))