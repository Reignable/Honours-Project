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

images = ['../images/100_ref_close.jpg']
for i in images:
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
    show_image(quant, 0)
    # Circle finding
    upper_bound = np.array([100, 100, 255])
    lower_bound = np.array([0, 0, 130])
    mask = cv2.inRange(quant, lower_bound, upper_bound)
    marker = cv2.bitwise_and(quant, quant, mask=mask)
    marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
    show_image(marker, 0)
    # Find contours
    cnts, _ = cv2.findContours(marker.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:2]
    (x,y),radius = cv2.minEnclosingCircle(cnts[0])
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(orig,center,radius,(0,255,0),2)

    x,y,w,h = cv2.boundingRect(cnts[1])
    cv2.rectangle(orig,(x,y),(x+w,y+h),(0,255,0),2)
    # cv2.drawContours(orig, cnts, -1, (0,255,0), 4)
    cv2.imwrite('output.jpg', orig)
    # Select lowest one

    #Get highest point of lowest contour

    #Measure to that point
