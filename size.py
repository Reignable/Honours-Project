'''
Ho = ((f * (Hi / Hs)) / (D - f)) * Hc

Ho = Height object
f  = Focal length mm
Hi = Height image pixels
Hs = Height sensor mm
D  = Distance of object from camera
Hc = Height camera from ground
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--height_object')
parser.add_argument('-f', '--focal_length', type=float)
parser.add_argument('-i', '--height_image', type=int)
parser.add_argument('-s', '--height_sensor', type=int)
parser.add_argument('-d', '--distance', type=int)
parser.add_argument('-c', '--height_camera', type=int)
args = parser.parse_args()
if not args.height_object:
    obj_height = (((args.focal_length * (args.height_image / args.height_sensor)) / (args.distance - args.focal_length)) * args.height_camera)
    print('Height of object is {h}'.format(h=obj_height))
