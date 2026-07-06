import numpy as np
import pandas as pd
import plotly.express as px


df = pd.read_csv("https://raw.githubusercontent.com/YBI-Foundation/Dataset/refs/heads/main/Salary%20Data.csv")
# print("Mean: ", data['Salary'].mean())
# print("\nVarience: ", data['Salary'].var())
# print("\nStandard Deviation: ", data['Salary'].std())

# fig = px.scatter(
#     df,
#     x="Experience Years",
#     y="Salary"
# )

fig = px.box(
    df,
    y="Salary"
)

fig.show()

