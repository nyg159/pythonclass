print("11-4.     20173087 노원진\n")
import math
import matplotlib.pyplot as plt
x = []
y = []
z = []
for angle in range(360):
    x.append(angle)
    z.append(math.cos(math.radians(angle)))
    y.append(math.sin(math.radians(angle)))
plt.plot(x, y)
plt.plot(x, z, 'r-')
plt.title("SINE & COSINE WAVE, 220173087, Noh won jon")
plt.show()

# math 모듈을 가져옵니다.
# pyplot 모듈을 plt로 가져옵니다.
# 빈 리스트 x, y, z를 생성합니다. 이들은 각각 각도(angle), 사인 값, 코사인 값의 리스트로 사용됩니다.
# for 루프를 사용하여 0부터 359까지의 각도를 반복합니다.
# angle 값을 x 리스트에 추가합니다.
# math.radians() 함수를 사용하여 각도를 라디안 값으로 변환한 뒤, math.sin() 함수와 math.cos() 함수를 사용하여 사인 값과 코사인 값 계산 후 각각 y와 z 리스트에 추가합니다.
# plt.plot() 함수를 사용하여 x, y로 사인 함수 그래프를 그리고, x, z로 코사인 함수 그래프를 그립니다.
# plt.title() 함수를 사용하여 그래프의 제목을 설정합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.