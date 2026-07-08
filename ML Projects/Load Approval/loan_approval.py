# Dataset
# | Age | Salary (₹) | Credit Score | Loan Approved |
# | --- | ---------: | -----------: | ------------- |
# | 25  |      30000 |          650 | No            |
# | 30  |      50000 |          700 | Yes           |
# | 22  |      25000 |          600 | No            |
# | 40  |      80000 |          750 | Yes           |
# | 35  |      60000 |          720 | Yes           |
# | 28  |      40000 |          680 | No            |
# | 45  |      90000 |          800 | Yes           |
# | 32  |      55000 |          710 | Yes           |

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv("loan_data.csv")

x = df[["Age","Salary","Credit Score"]]
y = df["Loan Approved"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=42)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

# prediction = model.predict([[29, 48000, 690]])

# print(prediction)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

print(accuracy)