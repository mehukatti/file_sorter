import os
import datetime
from sort_modes.date_sorter import DateSorter

def test_get_file_dates():
    path = "your path" # TODO
    if os.path.exists(path):
        print("Exists")
    else:
        print("Does not exist")
        raise Exception(f"The file {path} does not exist.")
    
    # file modification 
    timestamp = os.path.getmtime(path)

    # convert timestamp into DateTime object
    datestamp = datetime.datetime.fromtimestamp(timestamp)
    print('Modified Date/Time:', datestamp)

    # file creation 
    c_timestamp = os.path.getctime(path)

    # convert creation timestamp into DateTime object
    c_datestamp = datetime.datetime.fromtimestamp(c_timestamp)

    print('Created Date/Time on:', c_datestamp)

def test_date_sorter():
    root_folder = "your path" # TODO
    new_root_folder = "your path" # TODO
    file_type = "image"
    sorter = DateSorter(root_folder, new_root_folder, file_type)

def test():
    print(f"current path: {os.getcwd()}")
