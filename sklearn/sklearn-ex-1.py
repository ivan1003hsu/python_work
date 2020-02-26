import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

x,y = datasets.make_classification(n_samples=5000, n_features=2, n_informative=2, n_redundant=0,  n_clusters_per_class=1, random_state=0, scale=1000)

##plt.scatter(x[:,0],x[:,1],c=y)
##plt.show()


n_cv = range(100,500,100)
for cv in n_cv:

    svc = SVC(gamma='auto')
    tree = DecisionTreeClassifier()
    forest = RandomForestClassifier(n_estimators=20)
    models = [svc, tree, forest]

    for model in models:
        score = cross_val_score(model, x, y, cv=cv, scoring='accuracy')
        if model == svc:
            c='r'
        elif model == tree:
            c='g'
        else:
            c='b'
        plt.scatter(cv,score.mean(),c=c,marker='.')

    x1 = preprocessing.scale(x)

    svc = SVC(gamma='auto')
    tree = DecisionTreeClassifier()
    forest = RandomForestClassifier(n_estimators=20)
    models = [svc, tree, forest]

    for model in models:
        score = cross_val_score(model, x1, y, cv=cv, scoring='accuracy')
        if model == svc:
            c='r'
        elif model == tree:
            c='g'
        else:
            c='b'
        plt.scatter(cv,score.mean(),c=c,marker='x', alpha=0.3)
    print(cv)
plt.show()
score_1 = cross_val_score(svc,x,y)