import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("data/healthcare.csv")

# Rename target column if needed
df.rename(columns={"No-show": "No_show"}, inplace=True)

# Convert target to numeric
df["No_show"] = df["No_show"].map({"No": 0, "Yes": 1})

df["Gender"] = df["Gender"].map({"F": 0,"M": 1})

# Select features
features = [
 'Age',
 'Scholarship',
 'Hipertension',
 'Diabetes',
 'Alcoholism',
 'SMS_received',
 'Gender'
]

X = df[features]
y = df["No_show"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "machine_learning/model.pkl")

print("\nModel saved as machine_learning/model.pkl")
