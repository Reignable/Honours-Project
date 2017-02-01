import argparse
import cv2
import numpy
import sys
import PIL.Image
import PIL.ExifTags

args = None
op_sensor_height = 4.921
mm_per_pixel = 15.0/536.0


def show_image(image):
    """
    Displays the given image in a window
    :param image: The image to display, cv2.Mat
    :return: None
    """
    cv2.imshow(str(image), image)
    cv2.waitKey(0)


def process_image(image_path):
    """
    Applies the appropriate processes before analysis can be carried out
    :param image_path: File-path to the image to be processed
    :return: The processed image with edge detection applied
    """
    image = cv2.imread(image_path)
    gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
    edged = cv2.Canny(blurred, 0, 100, apertureSize=3)
    return edged


'''
def get_sensor_size(exif):
    # (Resolution in pixels / Focal plane resolution in dpi) X 25.4(mm / in) = size in mm
    # Do for hor and ver
    horizontal_measurement = None
    vertical_measurement = None
'''


def get_ref_point_width(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # upper_bound = numpy.array([65, 65, 255])
    # lower_bound = numpy.array([0, 0, 200])
    # mask = cv2.inRange(image, lower_bound, upper_bound)
    circles = cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, 1, 1)
    ref_point = circles[0][0]
    return ref_point[2]*2


def get_focal_length(exif):
    """

    :param exif:
    :return:
    """
    measurement, divisor = exif['FocalLength']
    return float(measurement)/float(divisor)


def get_exif(image_path):
    """

    :param image_path:
    :return:
    """
    image = PIL.Image.open(image_path)
    exif = {PIL.ExifTags.TAGS[k]: v
            for k, v in image._getexif().items()
            if k in PIL.ExifTags.TAGS}
    return exif


def get_measurement_px(image):
    """
    Measures the distance between the shock body and o-ring in pixels
    :param image: The image to measure
    :return: The measurement in px
    """
    min_line_length = 300
    max_line_gap = 1
    image_height, image_width = image.shape[:2]
    y_min = image_height
    y_max = 0
    lines = cv2.HoughLinesP(image, 1, numpy.pi / 180, 50, min_line_length, max_line_gap)
    for x1, y1, x2, y2 in lines[0]:
        if (x1 >= image_width / 2
            and y1 >= image_height / 3
            and y2 <= (image_height * 0.45)
                and abs(x1 - x2) <= 1):
            y_min = min(y_min, y1)
            y_max = max(y_max, y2)
    return y_max - y_min


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        '--image',
                        type=str,
                        action='store',
                        metavar='',
                        help='The path to the image you wish to use')
    parser.add_argument('-w',
                        '--weight',
                        type=int,
                        action='store',
                        metavar='',
                        help='The weight of the rider in chosen units')
    parser.add_argument('-s',
                        '--sag',
                        type=int,
                        action='store',
                        metavar='',
                        help='The desired sag percentage')
    parser.add_argument('-p',
                        '--pressure',
                        type=int,
                        action='store',
                        metavar='',
                        help='The pressure you have already put into your bike')
    global args
    args = parser.parse_args()
    if args.image is None:
        print 'This program requires an image'
        parser.print_help()
        sys.exit(1)
    '''
    image = process_image(args.image)
    print 'measurement is', get_measurement_px(image)*mm_per_pixel
    '''
    get_ref_point(args.image)

if __name__ == '__main__':
    main()
