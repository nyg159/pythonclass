import cv2

mask_img = cv2.imread('./data/mask_circle.png')
back_img = cv2.imread('./data/iceberg.png')

mask_img = cv2.resize(mask_img, (300,400))
back_img = cv2.resize(back_img, (300,400))

mask_AND = cv2.bitwise_and(mask_img, back_img)
mask_OR = cv2.bitwise_or(mask_img, back_img)
mask_XOR = cv2.bitwise_xor(mask_img, back_img)

cv2.imshow('mask', mask_img)
cv2.imshow('back', back_img)
cv2.imshow('mask and', mask_AND)
cv2.imshow('mask or', mask_OR)
cv2.imshow('mask xor', mask_XOR)

cv2.waitKey(0)
cv2.destroyAllWindows()