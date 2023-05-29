import numpy as np
import cv2

org = cv2.imread('./data/mandrill.png')

kernel1 = np.ones((5,5), np.float32) / 25
kernel2 = np.ones((7,7), np.float32) / 49

averagerd33 = cv2.filter2D(org, -1, kernel1)
averagerd99 = cv2.filter2D(org, -1, kernel2)

cv2.imshow('original', org)
cv2.imshow('filtered1', averagerd33)
cv2.imshow('filtered2', averagerd99)

cv2.waitKey(0)
cv2.destroyAllWindows()