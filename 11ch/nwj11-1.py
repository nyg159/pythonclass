print("11-1.     20173087 노원진\n")

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = [x for x in range(1000)]
y = np.random.rand(1000)
plt.title("Numbers (20173087, rand Noh won jon)")
plt.plot(x, y, 'r-', marker='o')

plt.show()