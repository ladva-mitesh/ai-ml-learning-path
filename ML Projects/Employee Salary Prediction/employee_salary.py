import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("employee_data.csv")

x = df[[
    "Age",
    "Experience (Years)",
    "Performance Score"
]]

y = df["Salary"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier()

model.fit(x_train,y_train)

prediction = model.predict([[29, 4, 80]])

print(prediction)