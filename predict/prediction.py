# file should contain a function `predict()`
# that will take your preprocessed data as an input and 
# return a price as output.


import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

def predict():
    #load the pickle
    model = pickle.load(open('model/trained_model.pickle', 'rb'))

    # predict
    prediction = model.predict(X)


    return prediction


      # fetch the clean_data
    # #convert into np
    
    #convert to json to post
