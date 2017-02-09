import argparse
import sys
from image_processor import ImageProcessor


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
    parser.add_argument('-t',
                        '--stroke',
                        type=float,
                        action='store',
                        metavar='',
                        help='')
    parser.add_argument('-d',
                        '--debug',
                        action='store_true')
    global args
    args = parser.parse_args()
    if args.image is None:
        print 'This program requires an image'
        parser.print_help()
        sys.exit(1)

    t = ImageProcessor()
    pixels_per_mm = t.get_ref_point_width(args.image) / 5
    img = t.process_image(args.image)
    measurement_px = t.get_measurement_px(img)
    measurement_mm = measurement_px / pixels_per_mm
    # get mm per psi
    mm_per_psi = t.get_mm_per_psi(measurement_mm)
    # get ideal psi
    ideal_psi = t.calc_ideal_pressure(mm_per_psi)
    if args.debug:
        print 'px/mm', pixels_per_mm
        print 'measurement_px', measurement_px
        print 'measurement_mm', measurement_mm
        print 'mm_per_psi', mm_per_psi
    print ideal_psi


if __name__ == '__main__':
    main()
