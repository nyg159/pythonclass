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
