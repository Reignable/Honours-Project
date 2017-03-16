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

images = ['../images/100_rs.jpg']
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
    # Find contours
    cnts, _ = cv2.findContours(marker.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:2]
    print cnts
    cv2.drawContours(orig, cnts, -1, (0,255,0), 5)
    cv2.imwrite('contours.jpg', orig)
