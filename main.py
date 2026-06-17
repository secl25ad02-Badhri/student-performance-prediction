import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

plt.scatter(df["Study_Hours"], df["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")

plt.show()