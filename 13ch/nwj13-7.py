import numpy as np
import cv2

org = cv2.imread('./data/mandrill.png')

averagerd55 = cv2.GaussianBlur(org, (5,5), 1)
averagerd77 = cv2.GaussianBlur(org, (7,7), 1)

cv2.imshow('original', org)
cv2.imshow('Gaussian 55', averagerd55)
cv2.imshow('Gaussian 77', averagerd77)

cv2.waitKey(0)
cv2.destroyAllWindows()