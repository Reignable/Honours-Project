import cv2
import cv2.cv as cv
from imutils import contours
import imutils
import numpy as np


def show_image(image):
    cv2.imshow(str(image), image)
    cv2.waitKey(0)

img = cv2.imread('150.jpg')
height, width = img.shape[:2]
img = cv2.resize(img, (width/4, height/4))
gray_scaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_scaled = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
edged = cv2.Canny(gray_scaled, 0, 100, apertureSize=3)

show_image(edged)

sensor_size = 3.0
im_height = len(img[0])
mm_per_pixel = sensor_size/im_height

min_line_length = 300
max_line_gap = 0

lines = cv2.HoughLinesP(edged, 1, np.pi/180, 50, min_line_length, max_line_gap)
'''
x1, y1, x2, y2 = lines[0][0]
if x1 == x2:
    print (y1-y2)*mm_per_pixel
else:
    print (x1-x2)*mm_per_pixel

'''
img_height, img_width = img.shape[:2]
print img_height*0.75
for x1, y1, x2, y2 in lines[0]:
    #if x > half image
    if x1 >= img_width/2 and y1 >= img_height/3 and y2 <= (img_height * 0.5) and abs(x1 - x2) <= 1:
        cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 2)

show_image(img)

cv2.destroyAllWindows()
