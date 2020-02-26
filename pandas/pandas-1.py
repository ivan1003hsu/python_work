import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4.0,5,6,7])
#print(s)

dates = pd.date_range('20200201',periods=10)
#print(dates)

df =pd.DataFrame(np.arange(40).reshape(10,4),index=dates,columns=['a','b','c','d'])
print(df)

df2 = pd.DataFrame({'A':1,'1':'A','C':[1,2,3]},index=['ㄅ','ㄆ','ㄇ'])
#print(df2)

print(df.a.sum())
