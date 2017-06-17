# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# load data
dataframe = pd.read_csv('housing_prices.csv')
dataframe = dataframe.drop(['index', 'price', 'sq_price'], axis=1)
dataframe = dataframe[0:10]

# add labels
dataframe.loc[:, 'y1'] = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1]
dataframe.loc[:, 'y2'] = dataframe['y1'] == 0
dataframe.loc[:, 'y2'] = dataframe['y2'].astype(int)
print dataframe

# prepare data for tensorflow (tensors)
# tensors are a generic version of vectors and matrices

# convert features into input tensor
inputX = dataframe.loc[:, ['area', 'bathrooms']].as_matrix()

# convert labels to input tensors
inputY = dataframe.loc[:, ['y1', 'y2']].as_matrix()

print
print inputX
print
print inputY

# hyperparameters
learning_rate = 0.000001
training_epochs = 2000
display_step = 50
n_samples = inputY.size


