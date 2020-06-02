"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020
This program returns the median difference for both the testing
and training data sets for each of the tree depths. 

"""


import numpy as np
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor


# paste your get_features_targets function here
def get_features_targets(data):
  features = np.zeros((data.shape[0],4))
  features[:,0] = data['u'] - data['g']
  features[:,1] = data['g'] - data['r']
  features[:,2] = data['r'] - data['i']
  features[:,3] = data['i'] - data['z']
  targets = data['redshift']
  return features, targets

# paste your median_diff function here
def median_diff(predicted, actual):
  median_diff = np.median(abs(predicted - actual))
  return median_diff

# Complete the following function
def accuracy_by_treedepth(features, targets, depths):
  # split the data into testing and training sets
  split = features.shape[0]//2
  train_targets = targets[:split]
  test_targets = targets[split:]
  
  train_features = features[:split]
  test_features = features[split:]
  
  # initialise arrays or lists to store the accuracies for the below loop
  train_diff, test_diff = [], []
  
  # loop through depths
  for depth in depths:
    # initialize model with the maximum depth. 
    dtr = DecisionTreeRegressor(max_depth=depth)

    # train the model using the training set
    dtr.fit(train_features, train_targets)
   
    # get the predictions for the training set and calculate their median_diff
    predictions1 = dtr.predict(train_features)
    train_diff.append(median_diff(train_targets, predictions1))
    
    # get the predictions for the testing set and calculate their median_diff
    predictions2 = dtr.predict(test_features)
    test_diff.append(median_diff(test_targets, predictions2))
    
  # return the accuracies for the training and testing sets
  return train_diff, test_diff

if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # Generate several depths to test
  tree_depths = [i for i in range(1, 36, 2)]

  # Call the function
  train_med_diffs, test_med_diffs = accuracy_by_treedepth(features, targets, tree_depths)
  print("Depth with lowest median difference : {}".format(tree_depths[test_med_diffs.index(min(test_med_diffs))]))
    
  # Plot the results
  train_plot = plt.plot(tree_depths, train_med_diffs, label='Training set')
  test_plot = plt.plot(tree_depths, test_med_diffs, label='Validation set')
  plt.xlabel("Maximum Tree Depth")
  plt.ylabel("Median of Differences")
  plt.legend()
  plt.show()