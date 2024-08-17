import sys
import argparse

from sort_modes.date_sorter import DateSorter
from common.exceptions import NotImplemented

def main():
    parser=argparse.ArgumentParser(description="File sorter.")
    print ('argument list', sys.argv)

    parser.add_argument("source_folder")
    parser.add_argument("new_folder")
    parser.add_argument("file_type")
    parser.add_argument("mode")
    
    args=parser.parse_args()
    # run the program depending on the arguments.

    if args.mode == "month_sort":
        print("month sorting.")
        sorter = DateSorter(args.source_folder, args.new_folder, args.file_type, test_mode=False)
    else:
        raise Exception("This mode is not implemented")
    return

if __name__ == "__main__":
    main()