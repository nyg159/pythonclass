print("11-6.     20173087 노원진\n")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 4, figsize=(10, 3))
plt.title("Graph, 20173087, Noh won jon")
x = [x for x in range(7, 13)]
y = [456, 492, 578, 599, 670, 854]

ax[0].bar(x, y)
ax[1].plot(x, y)
ax[2].scatter(x, y, marker='^')
ax[3].barh(x, y)

plt.show()

# plt.subplots() 함수를 사용하여 1행 4열의 서브플롯(fig, ax)을 생성합니다. figsize 매개변수는 그림의 크기를 설정합니다.
# plt.title() 함수를 사용하여 그래프의 제목을 설정합니다.
# x 리스트에는 7부터 12까지의 숫자를 저장합니다.
# y 리스트에는 해당 숫자에 대응하는 값들을 저장합니다.
# ax[0].bar() 함수를 사용하여 첫 번째 서브플롯에 막대 그래프를 그립니다.
# ax[1].plot() 함수를 사용하여 두 번째 서브플롯에 선 그래프를 그립니다.
# ax[2].scatter() 함수를 사용하여 세 번째 서브플롯에 산점도를 그립니다. marker 매개변수를 '^\u203e'로 설정하여 삼각형 모양의 마커를 사용합니다.
# ax[3].barh() 함수를 사용하여 네 번째 서브플롯에 수평 막대 그래프를 그립니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.