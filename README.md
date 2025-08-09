# HeartWise – 10-Year CHD Risk Prediction

HeartWise is a web application built with **Flask** that predicts your **10-year risk of Coronary Heart Disease (CHD)** using a machine learning model trained on health and lifestyle data.  
Enter your health information, and instantly receive a clear **Low Risk** or **High Risk** result.

---

## 📖 Theory

**Coronary Heart Disease (CHD)** is one of the leading causes of illness and death globally.  
The **10-year CHD risk** score estimates the likelihood of developing CHD within the next decade, based on risk factors such as:

- Age, Gender  
- Blood Pressure & Hypertension medication use  
- Cholesterol & Glucose levels  
- Smoking status & cigarettes per day  
- Body Mass Index (BMI)  
- Medical history (Stroke, Diabetes, Hypertension)  

HeartWise uses a **Ridge Regression** model trained on medical datasets to classify users into:
- `0` → Low 10-year CHD risk  
- `1` → High 10-year CHD risk  

By identifying high-risk individuals early, lifestyle changes and medical interventions can be applied to reduce heart disease likelihood.

---

## 🚀 Features

- Predicts **TenYearCHD** = `0` (Low risk) or `1` (High risk)  
- Simple HTML form for input  
- Styled, responsive interface with clear result messages  
- Works locally or can be deployed to the cloud  
- No personal data stored

---

## 🛠️ Installation & Setup

Clone the repository:
git clone https://github.com/your-username/heartwise-chd-prediction.git
cd heartwise-chd-prediction
