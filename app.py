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
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = str(prediction[0])
            return jsonify({"Wine quality prediction (rate out of 10)": prediction}), 200
    return jsonify({"msg": 
    'POST method with json'
    })

 
if __name__ == "__main__":
    app.run(debug=True)