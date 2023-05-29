print("13-1.     20173087 노원진\n")

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('./data/mandrill.png')
print(img)

image_plot = plt.imshow(img)
plt.show()


