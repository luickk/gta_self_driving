import numpy as np
from tqdm import tqdm
import glob
import re



numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def get_data(path):
    files = sorted(glob.glob('{}/*.npy*'.format(path)), key=numericalSort)

    merged_data = np.zeros((501, 2), dtype=np.float)

    for f in tqdm(files):
        try:
            data = np.load(f)

            merged_data = np.concatenate((merged_data,data))

        except Exception as e:
            raise e

    return merged_data

def form_data_x(data):

    data = np.ma.masked_equal(data, 0)
    x_batch = []
    for img in range(len(data)):
        x_batch.append(data[img])

    data = None
    x_final = np.array(x_batch, dtype=np.float32)
    x_final = x_final[0, :, :, :]
    return x_final


def form_data_y(data):

    data = np.ma.masked_equal(data, 0)
    y_batch = []
    for r in range(len(data)):
        y_batch.append(data[r])

    data = None
    y_final = np.array(y_batch)
    return y_final
