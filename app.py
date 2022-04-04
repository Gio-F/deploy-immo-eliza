
import os
import pickle
from flask import Flask, request , jsonify
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict
import pandas as pd

app = Flask(__name__)
#model = pickle.load(open('model/trained_model.pickle', 'rb'))

#`GET` request and return `"alive"` if the server is alive.
@app.route('/')
def home():
   return 'alive'

#`GET` request returning a string to explain what the `POST` expect (data and format).
@app.route("/predict")
def explanation():
    
    return """ 
    "rooms-number": int,
    "equipped-kitchen": Optional[bool],
    "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
"""


#`POST` request that receives the data of a house in JSON format.
@app.route("/predict", methods = ["POST"])
def user_input():

    
    try:
        req = request.get_json()
        data = req["data"]
    except (TypeError, KeyError) as ex:
        return jsonify(f"something's wrong with your data. Is it json? {ex}")
    # {
    #     "building-state": "NEW",
    #     "equipped-kitchen": true,
    #      "rooms-number": 5
    #  }
    #the above is sent to preprocessing/cleaning data and give dict
    clean_data = preprocess(data)
    #if clean_data #contains key error:
    if 'error' in clean_data.keys():
        return jsonify(f"{clean_data['error']}")
    else:
        # transform dict into dataframe so they
        # can be fed to the model in the right shape
        clean_dataframe = pd.DataFrame([clean_data])
        #print(clean_dataframe)
        
        #clean data fed to model for prediction
        prediction = predict(clean_dataframe)

    #API returns prediction
    return jsonify(f"Prediction is {prediction}")

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)



# TODO check how to return errors to user!!!
# ?validation? 
# ?pedantic library?