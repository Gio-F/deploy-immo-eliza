# deploy-immo-eliza


From the file app.py we created a docker image. 
We deployed the container for the web applications "app-im-el" on Heroku.

contains a create a clear README to explain where your API is hosted and how to interact with it. Don't forget to mention:

- What routes are available? With which methods?
- What kind of data is expected (How should they be formatted? What is mandatory or not?)
- What is the output of each route in case of success? What is the output in case of error?

***Routes available***

 -  GET  https://app-im-el.herokuapp.com/ 
        Return "alive" if the server is alive.
 -  GET  https://app-im-el.herokuapp.com/predict
 Returns a string to the user explaining the data format required for the prediction
 -  POST https://app-im-el.herokuapp.com/predict
        POST request that receives the data of a house in JSON format
  
  Example:
        ```{
         "building-state": "NEW",
         "equipped-kitchen": true,
         "rooms-number": 5
        }```


