"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020
This program generatse features and targets for the decision tree.
The data in the galaxy catalogue:
    colours: u-g, g-r, r-i, and i-z;
    eccentricity: ecc
    4th adaptive moments: m4_u, m4_g, m4_r, m4_i, and m4_z;
    50% Petrosian: petroR50_u, petroR50_r, petroR50_z;
    90% Petrosian: petroR90_u, petroR90_r, petroR90_z.
"""


import numpy as np

def generate_features_targets(data):
  # complete the function by calculating the concentrations

  targets = data['class']

  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']

  # fill the remaining 3 columns with concentrations in the u, r and z filters
  # concentration in u filter
  features[:, 10] = data['petroR50_u']/data['petroR90_u']
  # concentration in r filter
  features[:, 11] = data['petroR50_r']/data['petroR90_r']
  # concentration in z filter
  features[:, 12] = data['petroR50_z']/data['petroR90_z']

  return features, targets


if __name__ == "__main__":
  data = np.load('galaxy_catalogue.npy')

  features, targets = generate_features_targets(data)

  # Print the shape of each array to check the arrays are the correct dimensions. 
  print("Features shape:", features.shape)
  print("Targets shape:", targets.shape)