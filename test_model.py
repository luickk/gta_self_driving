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

model = cnn_model.googlenet(WIDTH, HEIGHT, 3, LR, output=8)
model.load('model_data/'+MODEL_NAME)



def main():
    agent = drive_worker()
    #agent.steering_acc="forward"

    while True:
        img = cv2.resize(screen_cap.grab_frame(size), (WIDTH,HEIGHT))
        model_prediction = model.predict([img.reshape(WIDTH, HEIGHT, 3)])[0]
        pred = np.array(model_prediction) * np.array([4.5, 1.8, 1.8, 0.1, 0.1, 0.1, 0.5, 0.5])
        #0: W
        #1: WA
        #2: WD
        #3: S
        #4: SA
        #5: SD
        #6: A
        #7: D
        print(pred)
        choice = np.argmax(pred)
        print(choice)
        if choice == 0:
            agent.steering_acc="forward"
            print('forward')
        if choice == 1:
            agent.steering_acc="forward_left"
            print('forward_left')
        if choice == 2:
            agent.steering_acc="forward_right"
            print('forward_right')
        if choice == 3:
            agent.steering_acc="backwards"
            print('backwards')
        if choice == 4:
            agent.steering_acc="backwards_left"
            print('backwards_left')
        if choice == 5:
            agent.steering_acc="backwards_right"
            print('backwards_right')
        if choice == 6:
            agent.steering_acc="forward_left"
            print('forward_left')
        if choice == 7:
            agent.steering_acc="forward_right"
            print('forward_right')

if __name__ == "__main__":
    main()
