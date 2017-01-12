import cv2
import cv2.cv as cv
from imutils import contours
import imutils
import numpy as np

img = cv2.imread('bike.jpg')
img = cv2.resize(img,(1000,600))

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grayscaled = cv2.GaussianBlur(grayscaled, (5, 5), 0)
edged = cv2.Canny(grayscaled, 10, 125)

#cnts = cv2.HoughCircles(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
circles = cv2.HoughCircles(edged.copy(), cv.CV_HOUGH_GRADIENT, 1, 20,
                            param1=50,param2=30,minRadius=140,maxRadius=150)

circles = np.uint16(np.around(circles))
orig = img.copy()
for c in circles[0,:]:
    cv2.circle(orig,(c[0],c[1]),c[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(orig,(c[0],c[1]),2,(0,0,255),3)
cv2.imshow('Circles', orig)
cv2.waitKey(0)
