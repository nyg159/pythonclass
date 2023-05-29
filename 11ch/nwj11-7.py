print("11-7.     20173087 노원진\n")
import numpy as np 
import matplotlib.pyplot as plt 
mu1, sigma1 = -10, 2
mu2, sigma2 = 0, 4
mu3, sigma3 = 10, 8
Gauss1 = mu1 + sigma1 * np.random.randn(10000)
Gauss2 = mu2 + sigma2 * np.random.randn(10000) 
Gauss3 = mu3 + sigma3 * np.random.randn(10000) 
plt.figure(figsize=(10,6)) 
plt.hist(Gauss1, bins=50, alpha=0.4)
plt.hist(Gauss2, bins=50, alpha=0.4)
plt.hist(Gauss3, bins=50, alpha=0.4)
plt.title("Histogram, 20173087, Noh won jon")
plt.show()

# mu1, sigma1 등 변수를 사용하여 세 개의 가우시안 분포의 평균과 표준편차를 설정합니다.
# np.random.randn() 함수를 사용하여 각 분포에 대해 10000개의 난수를 생성합니다.
# mu1, sigma1 등을 적용하여 실제 분포를 생성합니다.
# plt.figure(figsize=(10,6)) 코드를 사용하여 그래프의 크기를 설정합니다.
# plt.hist() 함수를 사용하여 세 개의 분포를 히스토그램으로 그립니다. bins 매개변수는 막대의 개수를 설정하고, alpha 매개변수는 투명도를 조절합니다.
# plt.title() 함수를 사용하여 그래프의 제목을 설정합니다.
# plt.show() 함수를 호출하여 그래프를 출력합니다.