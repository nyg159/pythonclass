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