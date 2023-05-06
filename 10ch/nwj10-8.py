print("10-8.     20173087 노원진\n")

import numpy as np

a = np.random.rand(3,3,3)
print('1) 배열 a :')
print(a,'\n')

print('2) a의 원소들 중 최댓값 : {0}\n'.format(np.max(a)))

print('3) a의 원소들 중 최댓값의 위치 : ',np.argmax(a))