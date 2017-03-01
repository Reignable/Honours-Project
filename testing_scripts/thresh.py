from sklearn.cluster import MiniBatchKMeans
import cv2
import numpy as np
import warnings

warnings.filterwarnings('ignore')

def show_image(image, wait_time):
    try:
        cv2.imshow(str(image), image)
        cv2.waitKey(wait_time)
        return 0
    except cv2.error as e:
        print e.message

images = ['../images/100_ref_fox.jpg']
for i in images:
    image = cv2.imread(i)
    orig = image.copy()
    (height, width) = image.shape[:2]
    print height
    print height/3
    '''
    # Color Quatification
    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = MiniBatchKMeans(n_clusters = 8)
    labels = clt.fit_predict(image)
    quant = clt.cluster_centers_.astype('uint8')[labels]
    quant = quant.reshape((h, w, 3))
    image = image.reshape((h, w, 3))
    quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
    cv2.imwrite('quant.jpg', quant)
    '''

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (T, thresh) = cv2.threshold(gray, 30, 150, cv2.THRESH_BINARY)
    cv2.imwrite('thresh.jpg', thresh)

    # Find contours
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    #cv2.drawContours(orig, cnts, -1, (0,255,0), 4)
    for cnt in cnts:
        x,y,w,h = cv2.boundingRect(cnt)
        if y > (height/3):
            print y
            cv2.rectangle(orig,(x,y),(x+w,y+h),(0,255,0),2)
    '''
    (x,y),radius = cv2.minEnclosingCircle(cnts[0])
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(orig,center,radius,(0,255,0),2)


    x,y,w,h = cv2.boundingRect(cnts[1])
    cv2.rectangle(orig,(x,y),(x+w,y+h),(0,255,0),2)
    # cv2.drawContours(orig, cnts, -1, (0,255,0), 4)
    '''
    cv2.imwrite('output.jpg', orig)
