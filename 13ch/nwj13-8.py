import numpy as np
import cv2


origianl_img = cv2.imread('./data/salt_pepper.png')
gauss_img = cv2.GaussianBlur(origianl_img,(9,9), 1)
bilateral_img = cv2.bilateralFilter(origianl_img, 9, 50, 50)
median_img = cv2.medianBlur(origianl_img, 9)

cv2.imshow('original', origianl_img)
cv2.imshow('Gaussian', gauss_img)
cv2.imshow('bilateral', bilateral_img)
cv2.imshow('median', median_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


