import numpy as np
import tensorflow as ts
import win32gui, win32ui, win32con, win32api
import cv2
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
    index = 0
    idx = []
    for img in range(len(data)):
        img_raw = np.any(data[img])
        if img_raw == 0.0:
            idx.append(index)
        index+=1
    data = np.delete(data, idx, axis=0)

    x_batch = []
    for img in range(len(data)):
        x_batch.append(data[img])

    x_final = np.array(x_batch, dtype=np.float32)
    x_final = x_final[0, :, :, :]
    return x_final
