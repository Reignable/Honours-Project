import cv2
import cv2.cv as cv
from imutils import contours
import imutils

img = cv2.imread('bike.jpg')
img = cv2.resize(img,(1000,600))

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grayscaled = cv2.GaussianBlur(grayscaled, (5, 5), 0)
edged = cv2.Canny(grayscaled, 10, 125)

#cnts = cv2.HoughCircles(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cv2.HoughCircles(edged.copy(), cv.CV_HOUGH_GRADIENT, 1, 20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

cnts = cnts[0] if imutils.is_cv2() else cnts[1]
(cnts, _) = contours.sort_contours(cnts)

for c in cnts:
    if cv2.contourArea(c) < 100:
        continue
    orig = img.copy()
    cv2.drawContours(orig, c, -1, (0, 255, 0), 2)
    cv2.imshow('cont', orig)
    cv2.waitKey(50)

cv2.destroyAllWindows()
