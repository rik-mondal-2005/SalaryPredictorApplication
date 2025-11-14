// Fixed backend API endpoint
const API_URL = "http://127.0.0.1:5000/predict";

// DOM elements
const form = document.getElementById("predictForm");
const submitBtn = document.getElementById("submitBtn");
const sampleBtn = document.getElementById("sampleBtn");
const errorBox = document.getElementById("error");
const resultBox = document.getElementById("result");
const salaryText = document.getElementById("salaryText");
const salaryBreakdown = document.getElementById("salaryBreakdown");
const themeToggle = document.getElementById("themeToggle");
const currentApi = document.getElementById("currentApi");

// Inputs
const ageEl = document.getElementById("age");
const expEl = document.getElementById("experience");
const genderEl = document.getElementById("gender");
const educationEl = document.getElementById("education");
const jobEl = document.getElementById("job_title");

// Load and apply theme
function loadTheme() {
  const theme = localStorage.getItem("theme") || "dark";
  if (theme === "light") {
    document.documentElement.classList.add("light");
    themeToggle.textContent = "🌞";
  } else {
    document.documentElement.classList.remove("light");
    themeToggle.textContent = "🌙";
  }
}
loadTheme();

// Toggle dark/light mode
themeToggle.addEventListener("click", () => {
  const isLight = document.documentElement.classList.toggle("light");
  localStorage.setItem("theme", isLight ? "light" : "dark");
  themeToggle.textContent = isLight ? "🌞" : "🌙";
});

// Smooth currency formatting
function formatCurrency(amount) {
  try {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
      maximumFractionDigits: 0
    }).format(amount);
  } catch {
    return "$" + Math.round(amount);
  }
}

// Show error box
function showError(msg) {
  errorBox.textContent = msg;
  errorBox.classList.remove("hidden");

  setTimeout(() => {
    errorBox.classList.add("hidden");
  }, 4500);
}

// Show result box
function showResult(salary, breakdown) {
  salaryText.textContent = formatCurrency(salary);
  salaryBreakdown.textContent = breakdown;

  resultBox.classList.remove("hidden");
}

// Fill sample data
sampleBtn.addEventListener("click", () => {
  ageEl.value = 30;
  expEl.value = 5;
  genderEl.value = "Male";
  educationEl.value = "Bachelor's";
  jobEl.value = "Software Engineer";
});

// Validate form
function validate(data) {
  if (data.age <= 20) 
    return "Age must be greater than 20.";

  if (data.experience < 0 || data.experience > 60)
    return "Experience must be between 0 and 60.";

  if ((data.age - data.experience) <= 20)
    return "Age - Experience must be greater than 20. Experience seems unrealistic.";

  if (data.job_title.length < 2)
    return "Please enter a valid job title.";

  return null;
}


// Handle submit
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorBox.classList.add("hidden");
  resultBox.classList.add("hidden");

  const payload = {
    age: Number(ageEl.value),
    gender: genderEl.value,
    education: educationEl.value,
    job_title: jobEl.value.trim(),
    experience: Number(expEl.value)
  };

  const validation = validate(payload);
  if (validation) return showError(validation);

  submitBtn.disabled = true;
  submitBtn.textContent = "Predicting…";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(`API Error: ${response.status} - ${text}`);
    }

    const data = await response.json();

    const salary = data.predicted_salary ?? data.salary;
    if (salary === undefined) throw new Error("Invalid response from server.");

    showResult(salary, `Prediction based on your input`);

  } catch (err) {
    console.error(err);
    showError(err.message || "Something went wrong.");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Predict Salary";
  }
});

// Display current API
currentApi.textContent = API_URL;
