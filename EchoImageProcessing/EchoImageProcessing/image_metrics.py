import os
import sys
from skimage import io
from skimage import measure
import numpy
import argparse
import time


def get_denoise_metrics(input, output, report):
    image_file_name1 = input
    image_file_name2 = output

    image_name1 = io.imread(image_file_name1)
    image_name2 = io.imread(image_file_name2)

    # estimate the standard deiviation of the images

    std_1 = numpy.std(numpy.std(numpy.array(image_name1)))
    std_2 = numpy.std(numpy.std(numpy.array(image_name2)))

    print("std is %2.10f" % std_1)

    # print ("Standard deviation of the images are"%(std_1,std_2))

    # estimate the peak signal to noise ratio (PSNR) between the image

    peak_signal_to_noise_ratio = measure.compare_psnr(image_name1, image_name2)

    print("Peak signal to noise ratio is %s" % peak_signal_to_noise_ratio)

    # estimate the mean square error between the images

    mse = measure.compare_mse(image_name1, image_name2)

    print("Mean square error between the images is %s" % mse)

    # estimate the normalised root mean square error between the images

    rmse = measure.compare_nrmse(image_name1, image_name2)

    print("Normalised root mean square error between the images is %s" % rmse)

    resp = open(report, 'w')
    resp.write("std1 is %2.10f \n" % std_1)
    resp.write("std2 is %2.10f \n" % std_2)
    resp.write(
        "Peak signal to noise ratio is %s \n" %
        peak_signal_to_noise_ratio)
    resp.write("Mean square error between the images is %s \n" % mse)
    resp.write(
        "Normalised root mean squre error between the images is %s \n" %
        rmse)
    resp.close()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", type=str,
                        help="increase output verbosity")

    parser.add_argument("-i", "--input", type=str, default="data_kidney",
                        help="input")

    parser.add_argument("-o", "--output", type=str, default='data_kidney.jpg',
                        help="output")

    parser.add_argument("-r", "--report", type=str, default='report.txt',
                        help="report path")

    args = parser.parse_args()

    get_denoise_metrics(args.input, args.output, args.report)


if '__main__' == __name__:
    main()
