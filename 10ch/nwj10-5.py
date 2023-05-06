print("10-5.     20173087 노원진\n")

import numpy as np

player = [[170, 76.4, 23],
          [183, 86.2, 24],
          [181, 78.5, 25],
          [176, 80.1, 26]]

np_player = np.array(player)

print('몸무게가 80 이상인 선수 정보')
print(np_player[np_player[:,1] >= 80.0])
print('키가 180 이상인 선수 정보')
print(np_player[np_player[:,0] >= 180])
print('나이가 25 이상인 선수 정보')
print(np_player[np_player[:,2] >= 25])

