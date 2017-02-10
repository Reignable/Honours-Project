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

    args = parser.parse_args()
    if args.image is None:
        print 'This program requires an image'
        parser.print_help()
        sys.exit(1)

    t = ImageProcessor(args.image, args.sag, args.pressure, args.stroke)
    pixels_per_mm = t.get_ref_point_width() / 5
    measurement_px = t.get_measurement_px()
    measurement_mm = measurement_px / pixels_per_mm
    inverse_mm = t.get_inverse_measurement(measurement_mm)
    # get mm per psi
    mm_per_psi = t.get_psi_per_mm(inverse_mm)
    # get ideal psi
    ideal_psi = t.calc_ideal_pressure(mm_per_psi)
    if args.debug:
        print 'px/mm', pixels_per_mm
        print 'measurement_px', measurement_px
        print 'measurement_mm', measurement_mm
        print 'desired mm', float(args.stroke) * (float(args.sag) / 100.0)
        print 'mm_per_psi', mm_per_psi
    print ideal_psi


if __name__ == '__main__':
    main()
