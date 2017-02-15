import cv2
import numpy

def show_image(image, wait_time):
    try:
        cv2.imshow(str(image), image)
        cv2.waitKey(wait_time)
        return 0
    except cv2.error as e:
        print e.message

image = cv2.imread('images/150_psi_ref.jpg')
upper_bound = numpy.array([75, 75, 255])
lower_bound = numpy.array([0, 0, 130])
mask = cv2.inRange(image, lower_bound, upper_bound)
marker = cv2.bitwise_and(image, image, mask=mask)
marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
show_image(marker, 0)
circles = cv2.HoughCircles(marker, cv2.cv.CV_HOUGH_GRADIENT, 3, 200)
orig = marker.copy()
for c in circles[0,:]:
    cv2.circle(orig,(c[0],c[1]),c[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(orig,(c[0],c[1]),2,(0,0,255),3)
# ref_point = circles[0][0]
# print ref_point
show_image(orig, 0)
#cv2.imwrite('output.jpg',image)
