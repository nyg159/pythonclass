print("10-9.     20173087 노원진\n")

import numpy as np

a = np.arange(0,32).reshape(4,4,2)
b = a.flatten()

print('a : ', a)
print('b : ',b)
print('10번째 원소 : ',b[9])
print('20번째 원소 : ',b[19])
