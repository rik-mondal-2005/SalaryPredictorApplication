# 📌 Salary Prediction Application

A full-stack **Machine Learning Salary Predictor** using a Flask backend and a modern animated frontend with dark/light mode.  
The system predicts employee salaries based on **age, gender, education, job title, and years of experience**.

## 🚀 Features

- 🎯 **Ensemble ML Model** (Random Forest, Gradient Boosting, Voting Regressor)  
- ⚡ **Flask REST API** for predictions  
- 🌓 **Dark / Light theme toggle**  
- 🎨 **Premium UI** (Amber → Orange → Rose gradient, glassmorphism)  
- 📱 **Responsive frontend**  
- ✔ **Real-time form validation**  
- ✔ **Salary prediction in milliseconds**  

## 🧠 Tech Stack

### Backend
- Python  
- Flask + Flask-CORS  
- Scikit-Learn  
- Pandas, NumPy  
- Joblib  

### Frontend
- HTML  
- CSS (Premium gradient + glassmorphism)  
- JavaScript ES6  

## 📂 Project Structure

```
backend/
│
├── api/
│   └── app.py
│
├── src/
│   ├── train_model.py
│   ├── predict.py
│   └── preprocess.py
│
├── models/
│   ├── salary_model.pkl
│   └── label_encoders.pkl
│
└── data/
    └── salary_dataset.csv

frontend/
├── index.html
├── index.css
└── index.js
```

## 🛠 Installation & Setup

### 1️⃣ Setup Virtual Environment

```bash
cd backend
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model
```bash
cd src
python train_model.py
```

### 4️⃣ Run the API
```bash
cd ../api
python app.py
```

API URL:
```
http://127.0.0.1:5000/predict
```

### 5️⃣ Run the Frontend

Open:
```
frontend/index.html
```

## 🧪 API Example

### Request
```
POST /predict
```

### JSON
```json
{
  "age": 30,
  "gender": "Male",
  "education": "Bachelor's",
  "job_title": "Software Engineer",
  "experience": 5
}
```

### Response
```json
{
  "predicted_salary": 92000
}
```

## 🌗 Dark/Light Theme

- ⚫ Dark Mode — premium deep gradient  
- ⚪ Light Mode — soft pastel gradient  
- ✨ Smooth animations  
- 🧊 Glassmorphism design  
- 📱 Fully responsive layout  



## ✨ Future Improvements

- Deploy backend to Render / Railway  
- Deploy frontend to Netlify / Vercel  
- Add job-title auto-suggestions  
- Add ML metrics dashboard  
- Add user login system  

## 👨‍💻 Author

**Rik Mondal**  
ML & Full-Stack Developer
