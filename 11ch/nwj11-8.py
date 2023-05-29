print("11-8.     20173087 노원진\n")
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2, figsize=(10, 3))

xData1 = 6 * np.random.randn(1000) + 25
yData1 = 6 * np.random.randn(1000) + 25

xData2 = 6 * np.random.randn(1000) + 25
yData2 = []
for value in xData2:
    yData2.append(value + np.random.randn())

ax[0].scatter(xData1, yData1)
ax[1].scatter(xData2, yData2, c='green')
plt.title("Scatter, 20173087, Noh won jon")

plt.show()

# plt.subplots() 함수를 사용하여 1행 2열의 서브플롯(fig, ax)을 생성합니다. figsize 매개변수는 그림의 크기를 설정합니다.
# np.random.randn() 함수를 사용하여 무작위로 생성된 값에 표준편차와 평균을 적용하여 xData1, yData1을 생성합니다.
# np.random.randn() 함수와 반복문을 사용하여 xData2에 표준편차를 적용한 값에 임의의 난수를 더하여 yData2를 생성합니다.
# ax[0].scatter() 함수를 사용하여 첫 번째 서브플롯에 xData1, yData1을 산점도로 그립니다.
# ax[1].scatter() 함수를 사용하여 두 번째 서브플롯에 xData2, yData2를 산점도로 그립니다. c 매개변수를 사용하여 색상을 초록색으로 지정합니다.
# plt.title() 함수를 사용하여 그래프의 제목을 설정합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.