print("10-2.     20173087 노원진\n")

import numpy as np

array_a = np.array([0,1,2,3,4,5,6,7,8,9])
print("실습 1 : array_a =", array_a)

array_b = np.array(range(10))
print("실습 1 : array_b =", array_b)

array_c = np.array(range(0,10,2))
print("실습 1 : array_c =", array_c)

print('실습 4 : ')
print('array_c 의 shape : ', array_c.shape)
print('array_c 의 ndim : ', array_c.ndim)
print('array_c 의 dtype : ', array_c.dtype)
print('array_c 의 size : ', array_c.size)
print('array_c 의 itemsize : ', array_c.itemsize)