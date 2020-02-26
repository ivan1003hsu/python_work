import numpy as np
result = ''
result = result.split(',')
result = list(map(float,result))
result_ = np.array(result)
result_ = result_.reshape(99,2)
import matplotlib.pyplot as plt
plt.plot(result_[:,0],result_[:,1])
plt.show()