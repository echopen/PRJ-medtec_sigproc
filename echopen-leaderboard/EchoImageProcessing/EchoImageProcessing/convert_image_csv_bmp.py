from .filereader import FileReader
from .scanconverter import ScanConverter


__author__ = 'mehdibenchoufi'


def run():
    file_reader = FileReader("kidney_data.csv")
    scanconversion = ScanConverter(file_reader)
    scanconversion.convert(file_reader)

run()
