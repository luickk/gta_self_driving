import numpy as np
import tensorflow as ts
from screen import screen_cap
import win32gui, win32ui, win32con, win32api
import cv2
import keyboard as kb
from data import data_prog
from tqdm import tqdm
from time import sleep
from key_worker import drive_worker

WIDTH = 480
HEIGHT = 270
LR = 0.00001
EPOCHS = 1000

MODEL_NAME = 'Pete'

#training data path
path = 'D:/data_ai/'

def main():
    dw = drive_worker()
    dw.steering_acc="forwad"

    sleep(2)
    dw.steering_acc="forwad_left"

    sleep(2)
    dw.steering_acc="forwad_right"

    sleep(10)
if __name__ == "__main__":
    main()
