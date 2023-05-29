print("10-8.     20173087 노원진\n")

import numpy as np

a = np.random.rand(3,3,3)
print('1) 배열 a :')
print(a,'\n')

print('2) a의 원소들 중 최댓값 : {0}\n'.format(np.max(a)))

print('3) a의 원소들 중 최댓값의 위치 : ',np.argmax(a))

# np.random.rand() 함수를 사용하여 3x3x3 형태의 난수로 구성된 배열을 생성하고, a 변수에 저장합니다.
# print() 함수를 사용하여 배열 a의 내용을 출력합니다.
# np.max() 함수를 사용하여 배열 a에서 최댓값을 찾고, 이를 출력합니다.
# np.argmax() 함수를 사용하여 배열 a에서 최댓값의 위치를 찾고, 이를 출력합니다.
# 이 코드는 numpy를 사용하여 3차원 배열을 생성하고, np.max() 함수를 통해 배열에서 최댓값을 찾습니다. 
# 또한, np.argmax() 함수를 사용하여 최댓값의 위치를 찾고 출력합니다.