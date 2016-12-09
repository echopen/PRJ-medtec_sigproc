__author__ = 'mehdibenchoufi'

import argparse
from filereader import FileReader
from data import Data
from constants import Constants
from filereader import FileReader

import cv2



def execution():

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", type=str,
                        help="increase output verbosity")

    parser.add_argument("-i", "--input", type=str, default="data_kidney",
                        help="input")

    parser.add_argument("-o", "--output", type=str, default='data_kidney.jpg',
                        help="output")

    args = parser.parse_args()

    file_reader = FileReader(args.input)
    scanconversion = ScanConverter(file_reader)
    scanconversion.convert(file_reader, args.output)


class ScanConverter:

    def __init__(self, file_reader):
        self.file_reader = file_reader
        self.data = Data()
        self.set_io(self.data)

    def get_input(self, value):
        return self.input

    def set_input(self, value):
        self.input = value

    def get_intermediate_input(self, value):
        return self.intermediate_input

    def set_intermediate_input(self, value):
        self.intermediate_input = value

    def get_output(self, value):
        return self.output

    def set_output(self, value):
        self.output = value

    def set_io(self, data):
        self.set_input(data.get_src())
        self.set_intermediate_input(data.get_intermediate_src())
        self.set_output(data.get_destination())

    def converter(self, filereader, output):
        cv2.linearPolar(
            self.intermediate_input,
            (Constants.CENTER_POINT_x,
             Constants.CENTER_POINT_z),
            Constants.SCAN_CONVERTER_SCALE,
            cv2.INTER_CUBIC + cv2.WARP_INVERSE_MAP,
            self.output)
        cv2.imwrite(output, self.output)
        # cv2.imshow('image',self.output)
        # cv2.waitKey(0)

    def convert(self, filereader, output):
        rows = self.data.get_rows()
        cols = self.data.get_cols()
        for i in range(0, rows):
            for j in range(0, cols):
                self.input[i, j] = filereader.pixel_array[i * cols + j]
                self.intermediate_input[
                    i,
                    j] = filereader.pixel_array[
                        i * cols + j]
        self.converter(filereader, output)



