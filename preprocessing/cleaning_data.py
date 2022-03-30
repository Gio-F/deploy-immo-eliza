# This file should contain a function called `preprocess()` 
# that will take a new house's data as input and return those data preprocessed as output.
# If your data doesn't contain the required information, you should return an error to the user.


#load pickel
#from json file in the POST req
# ```json
{
  "data": {
    "rooms-number": int,
    "equipped-kitchen": Optional[bool],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}
# ```
#     nparr = [ 
#  'Building condition',
#  'Kitchen type',
#  'Bedrooms']

 {
#   "data": {
#     "rooms-number": int, 'Bedrooms'
#     "equipped-kitchen": Optional[bool], 'Kitchen type'
#     "building-state": Optional[
#       "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
#     ], 'Building condition'
#   }



# Kit_type_dict = {"USA uninstalled" : 0, 
#                  "Not installed" : 0, 
#                  "Installed": 1, 
#                  "USA installed": 1,
#                  "Semi equipped": 1,
#                  "USA semi equipped": 1,
#                  "Hyper equipped": 2,
#                  "USA hyper equipped": 2
#                 }

# df = df.replace(Kit_type_dict)
# df["Kitchen type"] = df["Kitchen type"].fillna(0)

# """ building_condition_map = {'As new': 6, 'Just renovated': 5, 'Good': 4, 'To be done up': 3, 'To renovate':2, 'To restore':1}
# df = df.applymap(lambda s: building_condition_map.get(s) if s in building_condition_map else s)

# df['Building condition'].isnull().sum() """



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import requests

def preprocess(data):
    if "rooms-number" != int:
        print("you need to input an int")

    
    

    return clean_data

    
