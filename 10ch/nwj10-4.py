print("10-4.     20173087 노원진\n")

import numpy as np

x = np.array([[1.83, 1.76, 1.69, 1.86, 1.77, 1.73],
              [86.0, 74.0, 59.0, 95.0, 80.0, 68.0]])
y = x[0:2, 1:3]
z = x[0:2] [1:3]

bmi = x[1] / x[0]**2

print('x = ',x)
print('y = ',y)
print('z = ',z)
print('x shape : ',x.shape)
print('y shape : ',y.shape)
print('z shape : ',z.shape)
print('z values = : ',z)
print('BMI data')
print(bmi)

# x 배열에는 2x6 형태의 데이터가 저장되어 있습니다. 첫 번째 행은 키, 두 번째 행은 몸무게를 나타냅니다.
# y 배열은 x 배열의 첫 번째 행과 두 번째 행의 일부분을 슬라이싱하여 생성됩니다.
# z 배열은 x 배열의 일부분을 먼저 슬라이싱한 후, 다시 슬라이싱하여 생성됩니다.
# bmi 배열은 x 배열의 두 번째 행(몸무게)을 첫 번째 행(키)의 제곱으로 나눈 BMI 데이터를 계산합니다.
# print() 함수를 사용하여 x, y, z 배열의 내용과 형태(shape)를 출력합니다.
# print() 함수를 사용하여 z 배열의 내용을 출력합니다.
# print() 함수를 사용하여 BMI 데이터를 출력합니다.
# 이 코드는 numpy를 사용하여 배열을 생성하고, 배열 슬라이싱을 통해 원하는 부분을 추출합니다. 또한, 
# 산술 연산을 수행하여 BMI 데이터를 계산하고 출력합니다. 
# 배열의 형태(shape)를 확인하고, 필요한 데이터를 추출하는 기능을 활용하고 있습니다.