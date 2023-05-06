print("10-7.     20173087 노원진\n")

import numpy as np

n_arr = np.array([[0,1,2,3,4],
                  [5,6,7,8,9],
                  [10,11,12,13,14],
                  [15,16,17,18,19],
                  [20,21,22,23,24]])

narr = n_arr[0:2]

print('1) ',n_arr)

print('2)')
print('첫원소 : ',n_arr[0][0])
print('마지막 원소 : {} \n'.format(n_arr[-1][-1]))

print('3)')
print(n_arr[0:2],'\n')

print('4)')
print(n_arr[2:5],'\n')

print('5)')
print(n_arr[::1, ::2],'\n')

print('6)')
print(n_arr[::2, ::2],'\n')

print('7)')
print(narr.reshape(5,2))