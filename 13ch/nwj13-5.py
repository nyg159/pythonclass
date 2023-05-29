import numpy as np
import cv2

image = cv2.imread('./data/mandrill.png')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

red_low = np.array([-30,100,100])
red_high = np.array([30,255,255])

red_mask = cv2.inRange(image_hsv, red_low, red_high)
extracted = cv2.bitwise_and(image, image, mask=red_mask)

cv2.imshow('original',image)
cv2.imshow('red', red_mask)
cv2.imshow('extracted', extracted)

cv2.waitKey(0)
cv2.destroyAllWindows()