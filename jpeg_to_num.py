from PIL import Image
import pandas as pd
import numpy as np
import os

def image_to_arr(image_path):
    img = Image.open(image_path)
    arr = np.asarray(img, dtype="int32" )
    arr = list(arr)
    return arr

def run(data_path, csv_path):
    img_arr = []
    for filename in os.listdir(data_path):
        if "0" in filename:
            f = os.path.join(data_path, filename)
            img_arr.append(image_to_arr(f))
    df = pd.DataFrame({"img": img_arr})
    df.to_csv(os.path.join(csv_path, "data.csv"), encoding='utf-8', index=False)
    return df

        