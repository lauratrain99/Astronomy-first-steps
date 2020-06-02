"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020
This program uses our features and targets to train
a decision tree and then make a prediction.
We are going to use the DecisionTreeRegressor class from the sklearn.tree module.

"""


import numpy as np
from sklearn.tree import DecisionTreeRegressor

# copy in your get_features_targets function here
def get_features_targets(data):
  features = np.zeros((data.shape[0],4))
  features[:,0] = data['u'] - data['g']
  features[:,1] = data['g'] - data['r']
  features[:,2] = data['r'] - data['i']
  features[:,3] = data['i'] - data['z']
  
  targets = data['redshift']
  
  return features, targets

# load the data and generate the features and targets
data = np.load('sdss_galaxy_colors.npy')
features, targets = get_features_targets(data)
  
# initialize model
dtr = DecisionTreeRegressor()

# train the model
dtr.fit(features, targets)

# make predictions using the same features
predictions = dtr.predict(features)

# print out the first 4 predicted redshifts
print(predictions[:4])