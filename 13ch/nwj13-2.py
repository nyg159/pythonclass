import cv2

img = cv2.imread('./data/mandrill.png', 1)

cv2.line(img, (0,0), (200,200), (0,0,255), 5)
cv2.arrowedLine(img, (0,200),(200,20),(0,0,255), 5)
cv2.rectangle(img, (0,200),(200,20),(0,0,0),5)
cv2.putText(img, "hello!!!",(100,225), fontFace= 2, fontScale= 1, color=(0,0,0))
cv2.imshow('lined',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
