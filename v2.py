import argparse
import numpy

import cv2
import sys

args = None


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
    # Read in image
    image = cv2.imread(image_path)
    # Grayscale image
    gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur for cleaner lines
    blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
    # Apply canny edge detection
    edged = cv2.Canny(blurred, 0, 100, apertureSize=3)
    return edged


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
    parser.add_argument('-i',
                        '--image',
                        type=str,
                        action='store',
                        metavar='',
                        help='The path to the image you wish to use')
    global args
    args = parser.parse_args()
    if args.image is None:
        print 'This program requires an image'
        parser.print_help()
        sys.exit(1)
    image = process_image(args.image)
    print get_measurement_px(image)


if __name__ == '__main__':
    main()
