# Bloc_5-ML_in_production

## Project's presentation 🎥


## Context & Goals 🎯
* The data-science team has worked together on creating the best model predicting the quality score (from 0 to 10) of multiple wines. The next step is to include this model into the mobile application. The development team is expecting an API endpoint in order to request the model and display the result inside the application.

* Your job is to put the trained model into production, and so to provide:
    - a /predict endpoint,
    - a small documentation for the developer team at the index of your website.

## To access to the API and to predict the wine quality 📬
* The API documentation is reachable through the following link: https://wine-quality-meter-app.herokuapp.com/

* To get a prediction, as described above through the documentation, a terminal curl request is needed:
$ curl -i -H "Content-Type: application/json" -X POST -d '{"input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]}' https://wine-quality-meter-app.herokuapp.com/predict

* And you should see : 
$ {"Wine quality prediction (rate out of 10)":"6"}
