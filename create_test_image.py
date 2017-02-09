import cv2

base_image = cv2.imread('v4/test_image.jpg')
gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
edged = cv2.Canny(blurred, 0, 100, apertureSize=3)
