import cv2
import cv2.cv as cv
from imutils import contours
import imutils

img = cv2.imread('monarch.jpg')
img = cv2.resize(img, (500, 500))
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#grayscaled = cv2.GaussianBlur(grayscaled, (5, 5), 0)
edged = cv2.Canny(grayscaled, 50, 100)
#cv2.imshow('', edged)
#cv2.waitKey(0)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if imutils.is_cv2() else cnts[1]
(cnts, _) = contours.sort_contours(cnts)

for c in cnts:
    #if cv2.contourArea(c) < 100:
    #continue
    orig = img.copy()
    cv2.drawContours(orig, c, -1, (0, 255, 0), 2)
    cv2.imshow('cont', orig)
    cv2.waitKey(50)

cv2.destroyAllWindows()
