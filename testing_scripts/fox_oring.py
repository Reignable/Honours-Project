from sklearn.cluster import MiniBatchKMeans
import cv2
import numpy as np
import warnings

warnings.filterwarnings('ignore')

image = cv2.imread('../images/100_fox.jpg')
original = image.copy()
(height, width) = image.shape[:2]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(T, thresh) = cv2.threshold(gray, 30, 150, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
for contour in contours:
    x, y, h, w = cv2.boundingRect(contour)
    if y > (height / 3):
        cv2.rectangle(original, (x,y), (x+h,y+w), (0,255,0), 5)
cv2.imwrite('fox_oring.jpg', original)
