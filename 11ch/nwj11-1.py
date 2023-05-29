print("11-1.     20173087 노원진\n")

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = [x for x in range(1000)]
y = np.random.rand(1000)
plt.title("Numbers (20173087, rand Noh won jon)")
plt.plot(x, y, 'r-', marker='o')

plt.show()

# numpy의 난수 생성기에 시드(seed) 값을 0으로 설정합니다.
# x 리스트에는 0부터 999까지의 값을 저장합니다.
# np.random.rand() 함수를 사용하여 0부터 1 사이의 난수를 1000개 생성하여 y 리스트에 저장합니다.
# plt.title() 함수를 사용하여 그래프의 제목을 설정합니다. 제공된 제목은 학번과 학생의 이름으로 구성됩니다.
# plt.plot() 함수를 사용하여 x와 y 리스트를 연결하여 선 그래프를 그립니다. 'r-'는 빨간색 실선을 의미하고, marker 매개변수를 'o'로 설정하여 데이터 포인트를 원형 마커로 표시합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.