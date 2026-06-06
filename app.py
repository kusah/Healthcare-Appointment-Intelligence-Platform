# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():

#     if request.method == "POST":
#         print("Form Submitted!")

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
import joblib
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sah123",
    database="healthcare_db"
)

cursor = db.cursor()
app = Flask(__name__)

model = joblib.load("machine_learning/model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    probability = ""    
    if request.method == "POST":

        age = int(request.form["age"])
        gender = int(request.form["gender"])
        scholarship = int(request.form["scholarship"])
        hypertension = int(request.form["hypertension"])
        diabetes = int(request.form["diabetes"])
        alcoholism = int(request.form["alcoholism"])
        sms = int(request.form["sms"])

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

        if prediction == 1:
            result = "Likely No-Show"
        else:
            result = "Likely Show-Up"

        probability = round(probability * 100, 2)
        query = """
        INSERT INTO prediction_logs
        (age, gender, scholarship, hypertension,
        diabetes, alcoholism, sms_received,
        prediction, probability)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
        age,
        gender,
        scholarship,
        hypertension,
        diabetes,
        alcoholism,
        sms,
        result,
        probability
        )

        cursor.execute(query, values)
        db.commit()

    return render_template(
        "index.html",
        prediction=result if request.method == "POST" else "",
        probability=probability if request.method == "POST" else ""
    )

if __name__ == "__main__":
    app.run(debug=True)

# import joblib
# import pandas as pd

# model = joblib.load("machine_learning/model.pkl")

# importance = pd.DataFrame({
#     "Feature": model.feature_names_in_,
#     "Importance": model.feature_importances_
# })

# print(importance.sort_values("Importance", ascending=False))