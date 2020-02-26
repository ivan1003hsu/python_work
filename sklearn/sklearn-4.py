from sklearn.model_selection import learning_curve
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVC

digits = datasets.load_digits()
x=digits.data
y=digits.target

'''

train_sizes, train_loss, test_loss = learning_curve(SVC(gamma=0.001), x, y, cv=10, scoring='neg_mean_squared_error', train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
train_loss = -np.mean(train_loss,axis=1)
test_loss = -np.mean(test_loss,axis=1)

plt.plot(train_sizes,test_loss,c='g', label='test_loss')
plt.plot(train_sizes,train_loss,c='r', label='train_loss')

plt.xlabel('train_sizes')
plt.ylabel('error')
plt.show()

'''

#---------------------
from sklearn.model_selection import validation_curve

param_range = np.logspace(-6,-2.3 ,5)
train_loss, test_loss = validation_curve(SVC(),x, y, param_name='gamma', param_range=param_range, cv=10, scoring='neg_mean_squared_error')
train_loss = -np.mean(train_loss,axis=1)
test_loss = -np.mean(test_loss,axis=1)

plt.plot(param_range,test_loss,c='g', label='test_loss')
plt.plot(param_range,train_loss,c='r', label='train_loss')

plt.xlabel('gamma')
plt.ylabel('loss')
plt.show()