import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("student_data.csv")

X = df[["Study_Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

hours = float(input("Enter study hours: "))

prediction = model.predict(
    pd.DataFrame([[hours]], columns=["Study_Hours"])
)

print(f"Predicted Marks: {prediction[0]:.2f}")