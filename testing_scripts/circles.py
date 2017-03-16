import cv2
import numpy

def show_image(image, wait_time):
    try:
        cv2.imshow(str(image), image)
        cv2.waitKey(wait_time)
        return 0
    except cv2.error as e:
        print e.message

image = cv2.imread('../images/100_rs.jpg')
image_height, image_width = image.shape[:2]
upper_bound = numpy.array([90, 90, 255])
lower_bound = numpy.array([0, 0, 180])
mask = cv2.inRange(image, lower_bound, upper_bound)
marker = cv2.bitwise_and(image, image, mask=mask)
marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(marker, cv2.cv.CV_HOUGH_GRADIENT, 3, 500, minRadius=150, maxRadius=300)
orig = image.copy()
print circles[0]
for c in circles[0,:]:
    if c[1] <= image_height / 2:
        print c
        cv2.circle(orig,(c[0],c[1]),c[2],(0,255,0),5)
    # draw the center of the circle
        cv2.circle(orig,(c[0],c[1]),2,(0,0,255),5)
cv2.imwrite('HoughCircles.jpg',orig)
