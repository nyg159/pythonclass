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

# np.array() 함수를 사용하여 0부터 9까지의 값을 가지는 배열 array_a를 생성하고 출력합니다.
# np.array() 함수와 range() 함수를 사용하여 0부터 9까지의 값을 가지는 배열 array_b를 생성하고 출력합니다.
# np.array() 함수와 range() 함수를 사용하여 0부터 9까지의 값 중 짝수만을 가지는 배열 array_c를 생성하고 출력합니다.
# array_c 배열의 속성을 출력합니다:
# shape: 배열의 차원과 크기를 나타냅니다. 출력 결과는 (5,)로, 1차원 배열이며 원소가 5개임을 나타냅니다.
# ndim: 배열의 차원 수를 나타냅니다. 출력 결과는 1로, 1차원 배열임을 나타냅니다.
# dtype: 배열의 데이터 타입을 나타냅니다. 출력 결과는 int64로, 64비트 정수형 타입임을 나타냅니다.
# size: 배열의 전체 원소 수를 나타냅니다. 출력 결과는 5로, 원소가 5개임을 나타냅니다.
# itemsize: 배열의 각 원소의 크기를 나타냅니다. 출력 결과는 8로, 64비트 정수형 타입이므로 8바이트 크기임을 나타냅니다.
# 이 코드는 numpy를 사용하여 배열을 생성하고, 배열의 속성을 확인하는 기능을 수행합니다. 
# 배열의 차원, 크기, 데이터 타입, 원소 수, 원소 크기 등을 출력하여 배열의 특성을 알 수 있습니다.