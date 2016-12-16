import argparse
import os


def folder_calc(folder_raw, folder_processed):
    for i in os.listdir(folder_raw):
        if i.endswith('.csv') and ('processed_' + i) in os.listdir(folder_processed):
            print(
                "--------- SCORE for %s, against image processing %s is %s" % (i, 'processed_' + i,
                                                                               score_calculation(os.path.join(
                                                                                                 folder_raw, i), os.path.join(
                                                                                                 folder_processed, 'processed_' + i))
                                                                               ))
        else:
            print("A processed file is not available for this file : %s" % i)


def score_calculation(raw_datas, processed_datas):
    "will be replaced by a score calculation function"
    size_raw = os.path.getsize(raw_datas)
    size_processed = os.path.getsize(processed_datas)
    return size_raw / size_processed

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", type=str,
                        help="increase output verbosity")

    parser.add_argument("-r", "--raw_folder", type=str, default="raw_data",
                        help="raw_data")

    parser.add_argument(
        "-p", "--proc_folder", type=str, default='processed_data',
                        help="increase output verbosity")

    args = parser.parse_args()

    folder_calc(args.raw_folder, args.proc_folder)
