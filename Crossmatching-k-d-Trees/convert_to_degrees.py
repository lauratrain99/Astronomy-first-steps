"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program converts right ascension from HMS to decimal degrees and
declination from DMS to decimal degrees. 
"""

# Write your hms2dec and dms2dec functions here
import numpy as np
def hms2dec(hours, mins, seconds):
  return 15*(hours + mins/60 + seconds/(60*60))

def dms2dec(degrees, arcmin, arcsec):
  return abs(degrees) + arcmin/60 + arcsec/(60*60) if degrees > 0 else -1*(abs(degrees) + arcmin/60 + arcsec/(60*60))

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))