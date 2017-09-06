import numpy as np
import tensorflow as ts
from screen import screen_cap
from hardw import get_keys
import win32gui, win32ui, win32con, win32api
import cv2
import datetime
import pandas
import tables

def main():

    #where file is stored
    path = 'D:/data_ai/'

    #(left, top, res, res)
    size=(0,40,800,600)

    #Training data array
    tr_data = []

    #overall iterations
    itr = 0

    #step s
    save_steps = 500

    #done steps
    steps = 0

    paused = False

    while True:

        if get_keys.get_pause_key('T'):
            if paused:
                paused = False
            elif not paused:
                paused = True

        if not paused:

            itr += 1
            pressed_k = get_keys.get_pressed_keys()
            img = screen_cap.grab_frame(size)
            tr_data.append([img, pressed_k])
            print('Writing.. | Size: ', len(tr_data))

            if save_steps < len(tr_data):
                print('start saving')
                steps += 1
                np.save(path+'data'+str(steps)+'.npy', tr_data)
                print('----------------')
                print('Saved | Step: ', steps)
                print('----------------')
                tr_data = []

        elif paused:
            print('paused')
        #cv2.imshow('frame',img)

        if cv2.waitKey(1) & 0xFF == ord('q') or get_keys.get_stop_key('P'):
            break

    print('Saving data')
    print('Path:', path)

    #Saving
    np.save(path+'data'+str(steps)+'.npy', tr_data)
    print('----------------')
    print('Finally Saved | Step: ', steps)
    print('----------------')

if __name__ == "__main__":
    main()
