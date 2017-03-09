#! /usr/bin/env python

import cv2
import numpy
import warnings
from sklearn.cluster import MiniBatchKMeans

warnings.filterwarnings('ignore')

image = cv2.imread('images/100_rs.jpg')
raw_refs = image.copy()
raw_lines = image.copy()

# Edged
gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
edged = cv2.Canny(blurred, 10, 90, apertureSize=3)
cv2.imwrite('images_processed/edged.jpg', edged)
edged_refs = edged.copy()
edged_lines = edged.copy()

# Masked
(h, w) = image.shape[:2]
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
sized = image.reshape((lab.shape[0] * lab.shape[1], 3))
clt = MiniBatchKMeans(n_clusters=8)
labels = clt.fit_predict(sized)
quantified = clt.cluster_centers_.astype('uint8')[labels]
quantified = quantified.reshape((h, w, 3))
upper_bound = numpy.array([100, 100, 255])
lower_bound = numpy.array([0, 0, 130])
mask = cv2.inRange(quantified, lower_bound, upper_bound)
cv2.imwrite('images_processed/mask.jpg', mask)
marker = cv2.bitwise_and(image, image, mask=mask)
marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)

# Edged with boxes
# Raw with boxes
contours, _ = cv2.findContours(marker.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ref_point, oring = sorted(contours, key=cv2.contourArea, reverse=True)[:2]
(x,y),radius = cv2.minEnclosingCircle(ref_point)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(raw_refs,center,radius,(0,255,0),5)
cv2.circle(edged_refs,center,radius,(0,255,0),5)
x,y,w,h = cv2.boundingRect(oring)
cv2.rectangle(raw_refs,(int(x),int(y)),(x+w,y+h),(0,255,0),5)
cv2.rectangle(edged_refs,(int(x),int(y)),(x+w,y+h),(0,255,0),5)
cv2.imwrite('images_processed/raw_refs.jpg', raw_refs)

# Edged with lines
min_line_length = 1000
max_line_gap = 10
image_height, image_width = edged.shape[:2]
y_limit = x+h
y_min = image_height
y_max = 0
lines = cv2.HoughLinesP(edged,
                        1,
                        numpy.pi / 180,
                        50,
                        min_line_length,
                        max_line_gap)
for x1, y1, x2, y2 in lines[0]:
    if x1 >= image_width / 2 and \
                    y1 >= image_height / 3 and \
                    y2 <= ((image_height / 3)*2)+500 and \
                    abs(x1 - x2) <= 1:
        cv2.line(raw_lines, (x1, y1), (x2, y2), (0,255,0),5)
cv2.imwrite('images_processed/raw_lines.jpg', raw_lines)
