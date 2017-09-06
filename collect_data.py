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

    paused = False
    while True:

        if get_keys.get_pause_key('T'):
            if paused:
                paused = False
            elif not paused:
                paused = True
        itr += 1
        pressed_k = get_keys.get_pressed_keys()
        img = screen_cap.grab_frame(size)

        if not paused:
            print('writing..')
            tr_data.append([img, pressed_k])
        elif paused:
            print('paused')
        #cv2.imshow('frame',img)

        if cv2.waitKey(1) & 0xFF == ord('q') or get_keys.get_stop_key('P'):
            break

    file_name = path+'data'+str(itr)+'.npz'
    print('Saving data')
    print('Filename:', file_name)

    np.savez_compressed(file_name, tr_data)
    #decc: https://stackoverflow.com/questions/28276244/why-is-this-numpy-array-too-big-to-load


if __name__ == "__main__":
    main()
