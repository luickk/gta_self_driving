import numpy as np
import tensorflow as ts
from screen import screen_cap
import win32gui, win32ui, win32con, win32api
import cv2
import time
import keyboard as kb
from data import data_prog
from tqdm import tqdm
from key_worker import drive_worker
from screen import screen_cap
from model import cnn_model

WIDTH = 480
HEIGHT = 270

GAME_WIDTH = 800
GAME_HEIGHT = 600

#(left, top, res, res)
size=(0,40,GAME_WIDTH, GAME_HEIGHT)

LR = 0.00001
EPOCHS = 1000

MODEL_NAME = 'Pete'

#training data path
path = 'D:/data_ai/'

model = cnn_model.googlenet(WIDTH, HEIGHT, 3, LR, output=4)
model.load('model_data/'+MODEL_NAME)



def main():
    agent = drive_worker()
    #agent.steering_acc="forwad"

    while True:
        img = cv2.resize(screen_cap.grab_frame(size), (WIDTH,HEIGHT))
        model_prediction = model.predict([img.reshape(WIDTH, HEIGHT, 3)])[0]
        pred = np.array(np.around(model_prediction, decimals=1))
        for p in range(len(pred)):
            if pred[p] > 0.4:
                pred[p]=1
            elif pred[p] < 0.4:
                pred[p]=0
        pred = np.array(pred, int)
        print(pred)
        if pred[0] == 1 and pred[1] == 0 and pred[2] == 0 and pred[3] == 0:
            agent.steering_acc="forwad"
        if pred[0] == 1 and pred[1] == 1 and pred[2] == 0 and pred[3] == 0:
            agent.steering_acc="forwad_left"
        if pred[0] == 1 and pred[1] == 0 and pred[2] == 0 and pred[3] == 1:
            agent.steering_acc="forwad_right"
        if pred[0] == 0 and pred[1] == 0 and pred[2] == 1 and pred[3] == 0:
            agent.steering_acc="backwards"


if __name__ == "__main__":
    main()
