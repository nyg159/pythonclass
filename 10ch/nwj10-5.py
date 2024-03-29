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

# player 리스트에는 선수들의 키, 몸무게, 나이 데이터가 포함되어 있습니다.
# np.array() 함수를 사용하여 player 리스트를 numpy 배열로 변환하고, np_player 변수에 저장합니다.
# print() 함수를 사용하여 "몸무게가 80 이상인 선수 정보"를 출력합니다.
# np_player 배열에서 몸무게(np_player[:,1])가 80 이상인 선수들의 정보를 출력합니다.
# print() 함수를 사용하여 "키가 180 이상인 선수 정보"를 출력합니다.
# np_player 배열에서 키(np_player[:,0])가 180 이상인 선수들의 정보를 출력합니다.
# print() 함수를 사용하여 "나이가 25 이상인 선수 정보"를 출력합니다.
# np_player 배열에서 나이(np_player[:,2])가 25 이상인 선수들의 정보를 출력합니다.
# 이 코드는 numpy 배열을 활용하여 선수들의 키, 몸무게, 나이 데이터를 처리하고, 조건에 따라 필터링하여 해당하는 선수들의 정보를 출력합니다. 
# 선수들의 몸무게가 80 이상인 경우, 키가 180 이상인 경우, 나이가 25 이상인 경우에 해당하는 선수들의 정보를 출력합니다.