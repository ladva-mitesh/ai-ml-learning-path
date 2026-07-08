# Data :
# | Hours Studied | Result |
# | ------------- | ------ |
# | 1             | Fail   |
# | 2             | Fail   |
# | 3             | Fail   |
# | 4             | Pass   |
# | 5             | Pass   |
# | 6             | Pass   |
# | 7             | Pass   |
# | 8             | Pass   |

x = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [0]
]

y = [
    ["Fail"],
    ["Fail"],
    ["Fail"],
    ["Pass"],
    ["Pass"],
    ["Pass"],
    ["Pass"],
    ["Pass"],
    ["Fail"]
]

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=42)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

prediction = model.predict([[-1]])

print(prediction)

y_pred = model.predict(x_test)

accurcy = accuracy_score(y_test, y_pred)

print(accurcy)