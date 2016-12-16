__author__ = 'mehdibenchoufi'

from constants import Constants
import numpy as np


class Data:

    def get_rows(self):
        return self.rows

    def set_rows(self, value):
        self.rows = value

    def get_larger_rows(self):
        return self.larger_rows

    def set_larger_rows(self, value):
        self.larger_rows = value

    def get_cols(self):
        return self.cols

    def set_cols(self, value):
        self.cols = value

    def __init__(self, num_args=None):
        if num_args is None:
            self.set_rows(Constants.NUM_IMG_DATA)
            self.set_larger_rows(Constants.OPENCV_RELATIVE_ANGLE)
            self.set_cols(Constants.NUM_SAMPLES)
            self.set_dimension()
        else:
            self.set_rows(num_args[0])
            self.set_larger_rows(num_args[1])
            self.set_cols(num_args[2])
            self.set_dimension()

    def set_dimension(self):
        self.src_size = self.rows, self.cols
        self.intermediate_size = self.larger_rows, self.cols
        self.dest_size = self.larger_rows, self.cols

    def get_src(self):
        return np.zeros(self.src_size, dtype=np.uint8)

    def get_intermediate_src(self):
        return np.zeros(self.intermediate_size, dtype=np.uint8)

    def get_destination(self):
        return np.zeros(self.dest_size, dtype=np.uint8)
