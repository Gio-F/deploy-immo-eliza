# create a Flask API that contains:

# - A route at `/` that accept:
#   - `GET` request and return `"alive"` if the server is alive.
# - A route at `/predict` that accept:
#   - `POST` request that receives the data of a house in JSON format.
#   - `GET` request returning a string to explain what the `POST` expect (data and format).


import os
import pickle
from flask import Flask, request, jsonify
from preprocessing.cleaning_data import preprocess

app = Flask(__name__)
model = pickle.load(open('model/trained_model.pickle', 'rb'))

@app.route('/')
def home():
   return 'alive'

@app.route("/predict", methods = ["POST"])
def pred():

    req = request.get_json()
    
    data = dict(req["data"])
    # {
    #     "building-state": "NEW",
    #     "equipped-kitchen": true,
    #     "rooms-number": 5
    # }
   #the above is sent to preprocessing/cleaning data
    clean_data = preprocess(data)

    return

if __name__ == '__main__':
    app.run(port=5000)