from sklearn.linear_model import LinearRegression
import numpy as np

print("==== Battry backup ====")



X = np.array([[2000],[3000],[4000],[5000],[6000]])
Y = np.array([5,7,9,11,13])

model = LinearRegression()
model.fit(X,Y)
print(model.coef_)
print(model.intercept_)
n = int(input("Enter the mAH of the  battery: "))

Predict = model.predict([[n]])
print("Predicted backup time:", Predict)