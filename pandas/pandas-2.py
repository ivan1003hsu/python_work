import pandas as pd
import numpy as np

boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})

print(boys)
'''
   age   k
0    1  K0
1    2  K1
2    3  K2
'''
print(girls)
'''
   age   k
0    4  K0
1    5  K0
2    6  K3
'''

# 目前 age 欄位是重複的，我們為了要區別 boy 與 girl，必須要在新的合併表格中，為 age 欄位取新的名字
# 使用 suffixes 屬性即可辦到
res = pd.merge(boys,girls, on='k', suffixes=['_boy','_girl'], how='left')
print(res)
