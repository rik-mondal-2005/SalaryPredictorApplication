from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import sys
sys.path.append(os.path.abspath("../src"))
from predict import predict_salary
from preprocess import preprocess_input

app = Flask(__name__)
CORS(app)  # allow frontend to access API

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Salary Prediction API is running"}), 200

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # get data from request body

    age = data.get("age")
    gender = data.get("gender")
    education = data.get("education")
    job_title = data.get("job_title")
    experience = data.get("experience")

    processed = preprocess_input(age, gender, education, job_title, experience)  # preprocess input
    result = predict_salary(age, gender, education, job_title, experience)  # get predicted salary

    return jsonify({"predicted_salary": result})  # return salary in json

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
