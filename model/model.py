
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


df_15 = pd.read_csv('data_15feb.csv')

nparr = df_15.loc[ :,[ 'Price',
 'Building condition',
 'Kitchen type',
 'Bedrooms']]

features = [
 'Building condition',
 'Kitchen type',
 'Bedrooms']

target = 'Price'

X = nparr[features].values.reshape(-1, len(features))
Y = nparr[target].values


regressor = LinearRegression().fit(X, Y)
print(regressor.score(X, Y))

#create pickle file of trained model
filename = "trained_model.pickle"
pickle.dump(regressor, open(filename, "wb"))

