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

# np.array() 함수를 사용하여 5x5 형태의 다차원 배열을 생성하고, n_arr 변수에 저장합니다.
# n_arr 배열의 내용을 출력합니다.
# n_arr 배열에서 첫 번째 원소와 마지막 원소를 출력합니다.
# n_arr 배열의 첫 두 행을 추출하여 narr 변수에 저장하고 출력합니다.
# n_arr 배열의 3번째부터 마지막 행까지를 출력합니다.
# n_arr 배열에서 각 행의 첫 번째 원소와 세 번째 원소만을 선택하여 출력합니다.
# n_arr 배열에서 각 행과 열의 인덱스가 2의 배수인 원소들로 이루어진 부분 배열을 출력합니다.
# narr 배열을 5x2 형태로 재구성하여 출력합니다.
# 이 코드는 numpy를 사용하여 다차원 배열을 생성하고, 배열의 일부를 추출하거나 조작하여 원하는 부분을 출력합니다.
# 이를 통해 배열 슬라이싱, 인덱싱, 재구성 등의 기능을 활용할 수 있습니다.