import joblib
import pandas as pd

model = joblib.load("machine_learning/model.pkl")

##print("Features used by model:")
##print(model.feature_names_in_)

##exit()

print("Healthcare Appointment Predictor")
print("-" * 35)

age = int(input("Age: "))
gender = int(input("Gender (F=0, M=1): "))
scholarship = int(input("Scholarship (0/1): "))
hypertension = int(input("Hypertension (0/1): "))
diabetes = int(input("Diabetes (0/1): "))
alcoholism = int(input("Alcoholism (0/1): "))
sms = int(input("SMS Received (0/1): "))

patient = pd.DataFrame([{
    "Age": age,
    "Scholarship": scholarship,
    "Hipertension": hypertension,
    "Diabetes": diabetes,
    "Alcoholism": alcoholism,
    "SMS_received": sms,
    "Gender": gender
}])

prediction = model.predict(patient)[0]
probability = model.predict_proba(patient)[0][1]

print("\nPrediction Result")
print("-" * 20)

if prediction == 1:
    print("Likely No-Show")
else:
    print("Likely Show-Up")

print(f"No-Show Probability: {probability*100:.2f}%")