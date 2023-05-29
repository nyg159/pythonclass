print("10-10.     20173087 노원진\n")

import numpy as np

x1 = [ i for i in range(100)]
x2 = [ i + np.random.randint(1,10) for i in range(100)]
x3 = [ i + np.random.randint(1,50) for i in range(100)]
x4 = [ np.random.randint(1,100) for i in range(100)]

result = np.corrcoef([x1,x2,x3,x4])

print('x1 :')
print(x1,'\n')
print('x2 :')
print(x2,'\n')
print('x3 :')
print(x3,'\n')
print('x4 :')
print(x4,'\n')
print(result)

# x1 리스트에는 0부터 99까지의 값을 저장합니다.
# x2 리스트에는 0부터 99까지의 값에 1부터 10까지의 난수를 더하여 저장합니다.
# x3 리스트에는 0부터 99까지의 값에 1부터 50까지의 난수를 더하여 저장합니다.
# x4 리스트에는 1부터 99까지의 난수를 100번 생성하여 저장합니다.
# np.corrcoef() 함수를 사용하여 x1, x2, x3, x4 리스트들 간의 상관 계수를 계산합니다. 결과는 result 변수에 저장됩니다.
# print() 함수를 사용하여 x1, x2, x3, x4 리스트의 내용을 출력합니다.
# 마지막으로 result를 출력하여 상관 계수 결과를 확인합니다.
# 이 코드는 numpy를 사용하여 각각 다른 패턴의 난수로 구성된 리스트들을 생성하고, np.corrcoef() 함수를 통해 리스트들 간의 상관 계수를 계산합니다. 
# 생성된 리스트들과 계산된 상관 계수 결과를 출력하여 확인할 수 있습니다.