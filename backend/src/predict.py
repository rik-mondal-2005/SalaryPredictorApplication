import joblib
import numpy as np

# Load saved model and encoders
model = joblib.load("../models/salary_model.pkl")
label_encoders = joblib.load("../models/label_encoders.pkl")

# Predict salary function
def predict_salary(age, gender, education, job_title, experience):
    gender_encoded = label_encoders["Gender"].transform([gender])[0]        # encode gender
    edu_encoded = label_encoders["Education Level"].transform([education])[0]  # encode education
    job_encoded = label_encoders["Job Title"].transform([job_title])[0]     # encode job title

    input_data = np.array([[age, gender_encoded, edu_encoded, job_encoded, experience]])  # prepare input
    predicted_salary = model.predict(input_data)[0]  # get prediction

    return round(predicted_salary, 2)  # return formatted salary

# Test block
if __name__ == "__main__":
    result = predict_salary(
        age=30,
        gender="Male",
        education="Bachelor's",
        job_title="Software Engineer",
        experience=5
    )
    print("Predicted Salary:", result)
