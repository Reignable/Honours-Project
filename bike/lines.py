import cv2
import cv2.cv as cv
from imutils import contours
import imutils
import numpy as np

def show_image(image):
    cv2.imshow(str(image), image)
    cv2.waitKey(0)

img = cv2.imread('stan.jpg')
#img = cv2.resize(img, (500, 500))
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grayscaled = cv2.GaussianBlur(grayscaled, (5, 5), 0)
#edged = cv2.Canny(grayscaled, 50, 150, apertureSize = 3)
edged = cv2.Canny(grayscaled, 10, 200)

sensor_size = 3.0
im_height = len(img[0])
mm_per_pixel = sensor_size/im_height

min_line_length = 0
max_line_gap = 0

lines = cv2.HoughLinesP(edged, 1, np.pi/180, 100, min_line_length, max_line_gap)
x1, y1, x2, y2 = lines[0][0]
if x1 == x2:
    print (y1-y2)*mm_per_pixel
else:
    print (x1-x2)*mm_per_pixel

'''
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 2)
    show_image(img)
'''
cv2.destroyAllWindows()
