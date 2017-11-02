import numpy as np
import tensorflow as ts
import win32gui, win32ui, win32con, win32api

import glob
import sys
import cv2
import re
import time

#training data path
path = 'D:/data_ai/'

EPOCHS = 20000

WIDTH = 480
HEIGHT = 270

def main():

    files = sorted(glob.glob('{}/*.npy*'.format(path)), key=numericalSort)
    for e in range(EPOCHS):
        file_step = 0
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        for f in files:
            data_train = np.load(f)
            images = np.array([i[0] for i in data_train], dtype=np.uint8)
            for g in range((len(images))):
                image = images[g]
                cv2.imshow('image', image)
                cv2.waitKey(1)
                #time.sleep(0.3)

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

if __name__ == "__main__":
    main()
