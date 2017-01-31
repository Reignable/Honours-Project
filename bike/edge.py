import cv2

img = cv2.imread('150.jpg')
height, width = img.shape[:2]
img = cv2.resize(img, (width/2, height/2))
gray_scaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_scaled = cv2.GaussianBlur(gray_scaled, (5, 5), 0)

zero_fifty = cv2.Canny(gray_scaled, 0, 50)
zero_hundred = cv2.Canny(gray_scaled, 0, 100)
fifty_seventyfive = cv2.Canny(gray_scaled, 50, 75)
fifty_hundred = cv2.Canny(gray_scaled, 50, 100)
hundred_onefifty = cv2.Canny(gray_scaled, 100, 150)
'''
zero_fifty = cv2.resize(zero_fifty, (width/4, height/4))
zero_hundred = cv2.resize(zero_hundred, (width/4, height/4))
fifty_seventyfive = cv2.resize(fifty_seventyfive, (width/4, height/4))
fifty_hundred = cv2.resize(fifty_hundred, (width/4, height/4))
hundred_onefifty = cv2.resize(hundred_onefifty, (width/4, height/4))
'''
cv2.imshow('0, 50', zero_fifty)
cv2.imshow('0, 100', zero_hundred)
cv2.imshow('50, 75', fifty_seventyfive)
cv2.imshow('50, 100', fifty_hundred)
cv2.imshow('100, 150', hundred_onefifty)

cv2.waitKey(0)
cv2.destroyAllWindows()