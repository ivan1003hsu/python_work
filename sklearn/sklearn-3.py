import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

x,y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0,  n_clusters_per_class=1, random_state=0, scale=100)
##x=preprocessing.scale(x)

##plt.scatter(x[:,0],x[:,1],c=y )
##plt.show()


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
svc = SVC(gamma='auto')
svc.fit(x_train,y_train)

print(svc.score(x_test,y_test))
