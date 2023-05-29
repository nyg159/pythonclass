print("10-3.     20173087 노원진\n")

import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_weights/(np_heights**2)

print('대상자들의 키 : ', np_heights)
print('키가 1.80 이상인 사람 : {}'.format(np_heights[np_heights >= 1.80]))
print('대상자들의 몸무게 : ',np_weights)
print('몸무게가 85 이상인 사람 : {}'.format(np_weights[np_weights >= 85]))
print('대상자들의 BMI : ', bmi)
print('BMI가 27 이상인 사람 : {}'.format(bmi[bmi >= 27]))

# heights 리스트에는 대상자들의 키 데이터가, weights 리스트에는 대상자들의 몸무게 데이터가 저장되어 있습니다.
# np.array() 함수를 사용하여 heights 리스트를 numpy 배열로 변환하고, np_heights 변수에 저장합니다. 
# 동일하게 weights 리스트도 numpy 배열로 변환하여 np_weights 변수에 저장합니다.
# bmi 배열은 np_weights 배열을 np_heights 배열의 제곱으로 나눈 BMI 데이터를 계산합니다.
# print() 함수를 사용하여 대상자들의 키(np_heights), 키가 1.80 이상인 사람들의 키(np_heights[np_heights >= 1.80]), 대상자들의 몸무게(np_weights), 
# 몸무게가 85 이상인 사람들의 몸무게(np_weights[np_weights >= 85]), 대상자들의 BMI(bmi)를 출력합니다.
# 마지막으로 bmi 배열에서 BMI가 27 이상인 사람들의 BMI(bmi[bmi >= 27])를 출력합니다.
# 이 코드는 numpy를 사용하여 키와 몸무게 데이터를 처리하고, BMI를 계산하여 출력합니다. 특정 조건에 따라 키와 몸무게를 필터링하여 출력하고, 
# BMI 데이터에서 조건에 맞는 값들을 출력합니다. 
# numpy 배열을 활용하여 데이터 처리와 필터링을 간편하게 수행할 수 있습니다.