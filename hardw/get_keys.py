import numpy as np
import tensorflow as ts
from screen import screen_cap
import win32gui, win32ui, win32con, win32api
import cv2


keys = ['W']
for char in "WASD":
    keys.append(char)




def get_pressed_keys():
    pressed_keys = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    #0: W
    #1: WA
    #2: WD
    #3: S
    #4: SA
    #5: SD
    #6: A
    #7: D
    temp_keys = []
    for key in keys:
        if win32api.GetAsyncKeyState(ord(key)):
            temp_keys.append(key)

    if 'W' in temp_keys and 'A' in temp_keys:
        pressed_keys[1] = 1
    elif 'W' in temp_keys and 'D' in temp_keys:
        pressed_keys[2] = 1
    elif 'S' in temp_keys and 'A' in temp_keys:
        pressed_keys[4] = 1
    elif 'S' in temp_keys and 'D' in temp_keys:
        pressed_keys[5] = 1
    elif 'W' in temp_keys:
        pressed_keys[0] = 1
    elif 'S' in temp_keys:
        pressed_keys[3] = 1
    elif 'A' in temp_keys:
        pressed_keys[6] = 1
    elif 'D' in temp_keys:
        pressed_keys[7] = 1

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
