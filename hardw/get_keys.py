import numpy as np
import tensorflow as ts
from screen import screen_cap
import win32gui, win32ui, win32con, win32api
import cv2


keys = ['W']
for char in "WASD":
    keys.append(char)




def get_pressed_keys():
    pressed_keys = np.array([0, 0, 0, 0])
    #1: W
    #2: A
    #3: S
    #4: D

    for key in keys:
        if win32api.GetAsyncKeyState(ord(key)):
            if(key=='W'):
                pressed_keys[0]=1
            elif(key=='A'):
                pressed_keys[1]=1
            elif(key=='S'):
                pressed_keys[2]=1
            elif(key=='D'):
                pressed_keys[3]=1

    return pressed_keys

def get_stop_key(key='P'):
    pressed=False
    if win32api.GetAsyncKeyState(ord(key)):
        pressed=True
    return pressed

def get_pause_key(key='T'):
    pressed=False
    if win32api.GetAsyncKeyState(ord(key)):
        pressed=True
    return pressed
