import os
from jpeg_to_num import *

data_path = os.path.join(os.getcwd(), "data")
csv_path = os.getcwd()

if __name__ == "__main__":
    run(data_path, csv_path)