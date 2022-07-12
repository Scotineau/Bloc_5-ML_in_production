from flask import Flask, url_for, request, jsonify,render_template
import joblib

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory key
        if "input" in req.keys():
            # Load model
            classifier = joblib.load("./models/model.joblib")
            # Predict
            prediction = classifier.predict(req["input"])
            # Since prediction is a float and jsonify function can't handle
            # floats we need to convert it to string
            prediction = str(prediction[0])
            return jsonify({"predict": prediction}), 200
    return jsonify({"msg": 
    'POST method with json'
    })

 
if __name__ == "__main__":
    app.run(debug=True)
