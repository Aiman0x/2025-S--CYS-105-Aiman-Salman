import pandas as pd
from sklearn.linear_model import (LinearRegression)
data = pd.read_excel("Student_Attendance_Dataset.xlsx")
print(len(data))
C=["Lab 1","Lab 2","Lab 3","Lab 4","Lab 5",
   "Lab 6","Lab 7","Lab 8","Lab 9","Lab 10"]
data[C] = data[C].replace({"P":1,"A":0})
X = data[C]
Y = data["Final Marks"]
model = LinearRegression(X,Y)
n=[0,1,0,1,1,1,0,1,0,0]

