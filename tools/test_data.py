import numpy as np
import tensorflow as ts
import win32gui, win32ui, win32con, win32api

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from data import data_prog

#training data path
path = 'D:/data_ai/data5.py'

def main():

    data_train = data_prog.get_data(path)

    #Y
    batch_y = data_prog.form_data_y(np.array([i[1] for i in data_train], dtype=object))

    print(batch_y)

if __name__ == "__main__":
    main()
