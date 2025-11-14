import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor

# Load dataset
DATA_PATH = "../data/salary_dataset.csv"  
MODEL_DIR = "../models/"
df = pd.read_csv(DATA_PATH)

# Remove missing rows
df = df.dropna()

# Encode categorical columns
categorical_cols = ["Gender", "Education Level", "Job Title"]
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Prepare features and target
X = df[["Age", "Gender", "Education Level", "Job Title", "Years of Experience"]]
y = df["Salary"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Create ensemble models
rf = RandomForestRegressor(n_estimators=200, random_state=42)
gb = GradientBoostingRegressor(n_estimators=200, random_state=42)
voting_model = VotingRegressor([("rf", rf), ("gb", gb)])

# Train model
voting_model.fit(X_train, y_train)

# Create model directory if not exists
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# Save trained model and encoders
joblib.dump(voting_model, MODEL_DIR + "salary_model.pkl")
joblib.dump(label_encoders, MODEL_DIR + "label_encoders.pkl")

# Print completion message
print("Model trained and saved successfully.")
