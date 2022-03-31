# This file should contain a function called `preprocess()` 
# that will take a new house's data as input and return those data preprocessed as output.
# If your data doesn't contain the required information, you should return an error to the user.


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def preprocess(data):

  clean_data = {}

#check valid input & convert in data for model for Bedrooms
  if data["rooms-number"] == int:
    clean_data["Bedrooms"] = data["rooms-number"]
  else:
    print("you need to input an int") #check how to return this to user

#check valid input & convert in data for model for Kitchen type

  if data["equipped-kitchen"] == True:
    clean_data['Kitchen type'] = 1
  elif data["equipped-kitchen"] == False:
    clean_data['Kitchen type'] = 0
  else:
    print("you need to input true or false")

#check valid input & convert in data for model for Building condition

  if data["building-state"] == "NEW":
    clean_data['Building condition'] = 6
  elif data["building-state"] == "GOOD":
    clean_data['Building condition'] = 4
  elif data["building-state"] == "TO RENOVATE":
    clean_data['Building condition'] = 3
  elif data["building-state"] == "JUST RENOVATED":
    clean_data['Building condition'] = 5
  elif data["building-state"] == "TO REBUILD":
    clean_data['Building condition'] = 1
  else:
    print("""Please input one of the values from the following list, in capital letters:
    NEW
    GOOD
    TO RENOVATE
    JUST RENOVATED
    TO REBUILD""")  

  return clean_data