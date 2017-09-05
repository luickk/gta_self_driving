import numpy as np
import tensorflow as ts
from screen import screen_cap
import win32gui, win32ui, win32con, win32api
import cv2

def main():

    while True:
        size=(0,40,800,600)
        img = screen_cap.grab_frame(size)
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
