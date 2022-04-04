# deploy-immo-eliza

In app.py we used Flask API to build a REST API. 

The API checks the status of the server and returns predictions of house pricing based on the output of the trained regression model available in the "Predict" folder.

The original regression model and its training data are available in the "model" folder.

The function available in the "preprocessing" folder transforms the data received via the API in the correct format to be fed to the prediction model available in the "Predict" folder.

From the file app.py we created a docker image. 

We deployed the container for the web applications "app-im-el" on Heroku.

***Routes available***

 -  GET  https://app-im-el.herokuapp.com/ : Returns the string "alive" if the server is alive.
 
 -  GET  https://app-im-el.herokuapp.com/predict : Returns a string to the user explaining the data format required for the prediction.

Example: ""rooms-number": int, "equipped-kitchen": Optional[bool], "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"] "


 -  POST https://app-im-el.herokuapp.com/predict : Receives the data of a house in JSON format
  
  Example:
        ```{
         "building-state": "NEW",
         "equipped-kitchen": true,
         "rooms-number": 5
        }```
        
 


