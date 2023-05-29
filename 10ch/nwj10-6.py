print("10-6.     20173087 노원진\n")

import numpy as np

player = np.zeros((100,3))
player[:,0] = 10 * np.random.randn(100) + 175
player[:,1] = 10 * np.random.randn(100) + 70
player[:,2] = np.floor(10 * np.random.randn(100)) + 22

height = player[:,0]
heights = np.floor(player[:,0])
weight = player[:,1]
weights = np.floor(player[:,1])
age = player[:,2]
ages = np.floor(player[:,2])

print('신장 평균값 : ', np.mean(height))
print('신장 중앙값 : ', np.median(height))
print('신장 총계 : ', np.sum(heights))
print('체중 평균값 : ',np.mean(weight))
print('체중 중앙값 : ',np.median(weight))
print('체중 총계 : ',np.sum(weights))
print('나이 평균값 : ',np.mean(age))
print('나이 중앙값 : ',np.median(age))
print('나이 총계 : ',np.sum(ages))

# np.zeros() 함수를 사용하여 100x3 형태의 모든 요소가 0인 배열을 생성하고, player 변수에 저장합니다.
# player 배열의 첫 번째 열에는 평균값이 175, 표준편차가 10인 정규분포에서 생성된 데이터를 저장합니다. 이는 플레이어들의 신장을 나타냅니다.
# player 배열의 두 번째 열에는 평균값이 70, 표준편차가 10인 정규분포에서 생성된 데이터를 저장합니다. 이는 플레이어들의 체중을 나타냅니다.
# player 배열의 세 번째 열에는 평균값이 22, 표준편차가 10인 정규분포에서 생성된 데이터를 저장하고, 소수점 아래를 버립니다. 이는 플레이어들의 나이를 나타냅니다.
# player 배열의 첫 번째 열을 height 변수에 저장합니다.
# player 배열의 첫 번째 열의 소수점을 버린 값을 heights 변수에 저장합니다.
# player 배열의 두 번째 열을 weight 변수에 저장합니다.
# player 배열의 두 번째 열의 소수점을 버린 값을 weights 변수에 저장합니다.
# player 배열의 세 번째 열을 age 변수에 저장합니다.
# player 배열의 세 번째 열의 소수점을 버린 값을 ages 변수에 저장합니다.
# np.mean() 함수를 사용하여 height, weight, age 배열의 평균값을 계산하고 출력합니다.
# np.median() 함수를 사용하여 height, weight, age 배열의 중앙값을 계산하고 출력합니다.
# np.sum() 함수를 사용하여 heights, weights, ages 배열의 총계를 계산하고 출력합니다.
# 이 코드는 numpy를 사용하여 플레이어들의 신장, 체중, 나이 데이터를 생성하고, 이를 활용하여 평균값, 중앙값, 총계를 계산합니다. 각각의 결과는 출력되어 확인할 수 있습니다.
