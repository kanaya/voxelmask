import argparse
import cv2
import math
import numpy as np
import sys
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('vxl_file', help='VXL file (input)')
parser.add_argument('mask_image', help='mask image (input)')
parser.add_argument('output_vxl_file', help='VXL file (output)')
args = parser.parse_args()

vxl_filename = args.vxl_file
mask_image_filename = args.mask_image
output_vxl_filename = args.output_vxl_file

def mask_voxle(voxel, mask_image):
	# do something

def main():
	# Reading mask image
	print('Reading {}...'.format(mask_image_filename), end='', file=sys.stderr)
	mask_image = cv2.imread(mask_image_filename)
	print('done', file=sys.stderr)
	# Reading volumetric image
	print('Reading {}... '.format(vxl_filename), end='', file=sys.stderr)
	voxel = np.load(vxl_filename)
	print('done', file=sys.stderr)
	# Creating masked volumetric image
	masked_voxel = mask_voxel(voxel, mask_image)
	np.save(output_vxl_filename, masked_voxel)

if __name__ == '__main__':
	main()
