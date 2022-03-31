
import os
import pickle
from flask import Flask, request, jsonify
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

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
def pred():

    req = request.get_json()
    
    data = req["data"]
    # {
    #     "building-state": "NEW",
    #     "equipped-kitchen": true,
    #      "rooms-number": 5
    #  }
   
   
    #the above is sent to preprocessing/cleaning data
    clean_data = preprocess(data)

    #clean data fed to model for prediction
    prediction = predict(clean_data)
    #prediction = model.predict(clean_data)

    #API returns prediction
    return {jsonify(f"Prediction is {prediction}")}

if __name__ == '__main__':
    app.run(port=5000)