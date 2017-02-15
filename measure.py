import cv2
import numpy as np

def show_image(image, wait_time):
    try:
        cv2.imshow(str(image), image)
        cv2.waitKey(wait_time)
        return 0
    except cv2.error as e:
        print e.message

image = cv2.imread('images/100_psi_ref.jpg')
#image = cv2.resize(image, (500, 800))
gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
edged = cv2.Canny(blurred, 0, 100, apertureSize=3)

min_line_length = 500
max_line_gap = 10

lines = cv2.HoughLinesP(edged, 1, np.pi/180, 50, min_line_length, max_line_gap)

img_height, img_width = image.shape[:2]

y_min = img_height
y_max = 0

for x1, y1, x2, y2 in lines[0]:
    #if x > half image
    if x1 >= img_width/2 and y1 >= img_height/3 and y2 <= ((img_height / 3)*2) and abs(x1 - x2) <= 1:
        y_min = min(y1, y_min)
        y_max = max(y2, y_max)
        cv2.line(image, (x1, y1), (x2, y2), (0,255,0), 2)
cv2.imwrite('output.jpg',image)
