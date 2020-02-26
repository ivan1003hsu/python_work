from sklearn.externals import joblib
clf = joblib.load('save/knn.pkl')

from sklearn.datasets import load_iris

x = load_iris().data

print(clf.predict(x))