import cv2

img = cv2.imread('bike.jpg')
img = cv2.resize(img,(1000,600))
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptive = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('img', adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()
