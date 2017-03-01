#! /usr/bin/env python

import argparse
import multiprocessing as mp
import sys
import warnings
from image_processor import ImageProcessor
from pressure_calculator import PressureCalculator

warnings.filterwarnings('ignore')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        '--image',
                        type=str,
                        nargs=2,
                        action='store',
                        metavar='',
                        help='The path to the image you wish to use')
    parser.add_argument('-c',
                        '--colour',
                        type=str,
                        action='store',
                        metavar='',
                        help='The colour of the o-ring on the shock')
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

    image_processor = ImageProcessor(args.colour, args.debug)
    pressure_calculator = PressureCalculator(args.sag, args.stroke, args.debug)
    pressure_calculator.measurement_100 = image_processor.get_measurement(args.image[0])
    image_processor = ImageProcessor(args.colour, args.debug)
    pressure_calculator.measurement_150 = image_processor.get_measurement(args.image[1])
    #pressure_calculator.measurement_100 = 30.0
    #pressure_calculator.measurement_150 = 20.0
    print pressure_calculator.calculate()

if __name__ == '__main__':
    main()
