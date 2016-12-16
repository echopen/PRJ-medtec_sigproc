import os
import sys
import argparse
from skimage import io
from skimage import filter
from skimage import restoration


def denoise_image(input, output):
    kidney_image = io.imread(input)
    # estimate the noise in the image
    # do a test denosing using a total variation filter
    kidney_image_denoised_tv = restoration.denoise_tv_chambolle(
        kidney_image, weight=0.1)
    io.imsave(output, kidney_image_denoised_tv)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", type=str,
                        help="increase output verbosity")

    parser.add_argument("-i", "--input", type=str, default="data_kidney",
                        help="input")

    parser.add_argument("-o", "--output", type=str, default='data_kidney.jpg',
                        help="output")

    args = parser.parse_args()

    denoise_image(args.input, args.output)


if __name__ == '__main__':
    main()
