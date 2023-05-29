print("11-3.     20173087 노원진\n")
import matplotlib.pyplot as plt
x = [x / 10 for x in range(20)]        
y = [(x / 10)**2 for x in range(20)]   
z = [(x / 10)**3 for x in range(20)]   
i = [2**(x / 10) for x in range(20)]   

plt.title('20173087, Noh won jon')
plt.plot(x, x, label='linear')
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='qubic')
plt.plot(x, i, label='power')

plt.xlabel('x label')   
plt.ylabel('y label')

plt.legend()           
plt.show()

# plt.title() 함수를 사용하여 그래프의 제목을 설정합니다. 제공된 제목은 학번과 학생의 이름으로 구성됩니다.
# x 리스트는 0부터 1까지 0.1씩 증가하는 값을 저장합니다.
# y 리스트는 x의 각 값의 제곱 값을 저장합니다.
# z 리스트는 x의 각 값의 세제곱 값을 저장합니다.
# i 리스트는 2를 x의 각 값에 대해 제곱한 값을 저장합니다.
# plt.plot() 함수를 사용하여 x와 x, y, z, i 리스트를 각각 연결하여 선 그래프를 그립니다. 각 그래프에 대한 라벨(label)도 설정됩니다.
# plt.xlabel() 함수를 사용하여 x축의 레이블을 설정합니다.
# plt.ylabel() 함수를 사용하여 y축의 레이블을 설정합니다.
# plt.legend() 함수를 사용하여 그래프의 범례를 표시합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.