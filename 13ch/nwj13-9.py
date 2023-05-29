import numpy as np
import cv2

img1 = cv2.imread('./data/green_back.png')
img2 = cv2.imread('./data/iceberg.png')

front_img = cv2.resize(img1, (300,400))
back_img = cv2.resize(img2, (300,400))

img_hsv = cv2.cvtColor(front_img, cv2.COLOR_BGR2HSV)
l_bound = np.array([40, 100, 50])
u_bound = np.array([80, 255, 255])

my_mask = cv2.inRange(img_hsv, l_bound, u_bound)
mask_inv = cv2.bitwise_not(my_mask)

extracted = cv2.bitwise_and(front_img, front_img, mask=my_mask)

removed = cv2.bitwise_and(front_img, front_img, mask=mask_inv)

background = cv2.bitwise_and(back_img, back_img, mask=my_mask)

merged = cv2.bitwise_or(removed,background)

cv2.imshow('mask', my_mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('removed', removed)
cv2.imshow('background', background)
cv2.imshow('merged',merged)
cv2.imshow('extracted', extracted)

cv2.waitKey(0)
cv2.destroyAllWindows()