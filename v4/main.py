#! /usr/bin/env python

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

    image_processor = ImageProcessor(args.image, args.sag, args.pressure, args.stroke, args.debug)
    print image_processor.calc_ideal_pressure()


if __name__ == '__main__':
    main()
