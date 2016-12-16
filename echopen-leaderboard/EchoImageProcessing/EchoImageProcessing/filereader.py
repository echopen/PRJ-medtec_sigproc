__author__ = 'mehdibenchoufi'

import csv
import os


class FileReader:

    def __init__(self, name_file):
        self.pixel_array = []
        self.name_file = name_file
        self.open_file()

    def open_file(self):
        with open(self.name_file, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                for pixels in row:
                    self.pixel_array.append(int(pixels))
