import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris  = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

knn = ＫNeighborsClassifier()
knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)

correct = [y_test == y_predict]
print(correct)


print('------------')
from sklearn.model_selection import cross_val_score
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, x, y, cv=5, scoring='accuracy')  #scoring='neg_mean_squared_error ' ,for regression
print(scores.mean())


#save
from sklearn.externals import joblib
joblib.dump(knn, 'save/knn.pkl')
