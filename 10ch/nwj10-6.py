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