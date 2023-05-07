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
