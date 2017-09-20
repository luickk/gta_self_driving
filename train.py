import numpy as np
import tensorflow as ts
from screen import screen_cap
import win32gui, win32ui, win32con, win32api
import cv2
import glob
import re

from model import cnn_model
from data import data_prog
from tqdm import tqdm

WIDTH = 480
HEIGHT = 270
LR = 0.0000001
EPOCHS = 30000

MODEL_NAME = 'Pete'

#training data path
path = 'D:/data_ai/'

def main():
    model = cnn_model.googlenet(WIDTH, HEIGHT, 3, LR, output=8, model_name=MODEL_NAME)


    files = sorted(glob.glob('{}/*.npy*'.format(path)), key=data_prog.numericalSort)
    for e in tqdm(range(EPOCHS)):


        for f in files:
            data = np.load(f)
            data_train = data

            print('File size: ',len(data_train))
            #Y
            batch_y = data_prog.form_data_y(np.array([i[1] for i in data_train], dtype=object))

            #X
            batch_x = data_prog.form_data_x(np.array([i[0] for i in data_train], dtype=object)).reshape(-1,WIDTH,HEIGHT,3)

            model.fit({'input': batch_x}, {'targets': batch_y}, n_epoch=1, snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

        if e%100==0:
            print('###################-Model-Saved-###################')
            model.save('model_data/'+MODEL_NAME)

    print('###################-Finished-Learning-###################')
    model.save('model_data/'+MODEL_NAME)



if __name__ == "__main__":
    main()
