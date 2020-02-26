from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

boston = datasets.load_boston()
x = boston.data
y = boston.target

lr = LinearRegression(normalize=False)
lr.fit(x,y)
print('這是x中各參數的權重：',end='')
print(lr.coef_)  
print('這是回歸線與y軸的焦點',end='')
print(lr.intercept_)
print('這是lr設定的參數',end='')
print(lr.get_params)
print('這是為預測表現打分（百分比')
print(lr.score(x,y))