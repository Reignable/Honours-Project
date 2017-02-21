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

images = ['../images/150_psi_ref.jpg']
for i in images:
    print i
    image = cv2.imread(i)
    orig = image.copy()
    (h, w) = image.shape[:2]

    # Color Quatification
    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = MiniBatchKMeans(n_clusters = 8)
    labels = clt.fit_predict(image)
    quant = clt.cluster_centers_.astype('uint8')[labels]
    quant = quant.reshape((h, w, 3))
    image = image.reshape((h, w, 3))
    quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
    # Circle finding
    upper_bound = np.array([75, 75, 255])
    lower_bound = np.array([0, 0, 130])
    mask = cv2.inRange(quant, lower_bound, upper_bound)
    marker = cv2.bitwise_and(quant, quant, mask=mask)
    marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
    #input image, method, dp, mindist, sensitivity, edges
    circles = cv2.HoughCircles(marker, cv2.cv.CV_HOUGH_GRADIENT, 4, 200, maxRadius=(300/2),     minRadius=(280/2), param1=250, param2=90)
    if circles == None:
        print 'No circles'
    else:
        for c in circles[0,:]:
            cv2.circle(orig,(c[0],c[1]),c[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(orig,(c[0],c[1]),2,(0,0,255),3)
        show_image(orig, 0)
