import joblib
import numpy as np

# Load saved encoders
label_encoders = joblib.load("../models/label_encoders.pkl")

# Preprocess input data for prediction
def preprocess_input(age, gender, education, job_title, experience):
    gender_encoded = label_encoders["Gender"].transform([gender])[0]      # encode gender
    edu_encoded = label_encoders["Education Level"].transform([education])[0]  # encode education
    job_encoded = label_encoders["Job Title"].transform([job_title])[0]  # encode job title

    input_array = np.array([[age, gender_encoded, edu_encoded, job_encoded, experience]])  # combine all inputs
    return input_array  # return numpy array
