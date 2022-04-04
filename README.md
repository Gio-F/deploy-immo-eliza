# deploy-immo-eliza

### Description

This deployment is part of a training project at [BeCode](https://becode.org/). The objective is to deploy a machine learning model using REST API.
The tools to be used are Flask API, Docker and Heroku.



In app.py we used Flask to build a REST API. 

The API checks the status of the server and returns predictions of house pricing. This is based on the output of the trained regression model available in the *"predict"* folder. Alternatively, it'll show an error message if the data format is not the expected one.

The function available in the *"preprocessing"* folder transforms the user inputs received via the API in the correct format to be fed to the prediction model available in the *"predict"* folder.  If the values from the user input differs from the expected answers, the program will return an error message, displayed via the API.

The original regression model and its training data are available in the *"model"* folder.

From the file app.py we created a [docker](https://www.docker.com/) image (see Dockerfile and requirements.txt in the repository).

We deployed the container for the web applications *"app-im-el"* on [Heroku](https://www.heroku.com/).


### Routes available

 -  GET  https://app-im-el.herokuapp.com/ : Returns the string "alive" if the server is alive.
 
 -  GET  https://app-im-el.herokuapp.com/predict : Returns a string to the user explaining the values format required for the prediction.

>"rooms-number": int, "equipped-kitchen": Optional[bool], "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"] 


 -  POST https://app-im-el.herokuapp.com/predict : Receives the data of a house in JSON format
  
  Example:
        ```{
         "building-state": "NEW",
         "equipped-kitchen": true,
         "rooms-number": 5
        }```
        
 


