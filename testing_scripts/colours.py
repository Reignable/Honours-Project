import cv2
import numpy as np

lbound = np.uint8([[[0, 0, 130]]])
ubound = np.uint8([[[75, 75, 255]]])

lbound = cv2.cvtColor(lbound, cv2.COLOR_HSV2BGR)
ubound = cv2.cvtColor(ubound, cv2.COLOR_HSV2BGR)

print lbound
print ubound
