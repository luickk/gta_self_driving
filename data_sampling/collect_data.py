import numpy as np
import cv2
import sys
import glob
import time

from optparse import OptionParser
from hardw import get_keys
from PIL import ImageGrab

def main():

    #where file is stored
    #path = 'D:/data_ai/'
    path = 'C:/Users/MrGrimod/Desktop/gta_self_driving_v2/data_d/'

    #(left, top, res, res)
    size=(0,40,800,600)

    #Training data array
    tr_data = []

    #overall iterations
    itr = 0

    #step s
    save_steps = 500

    #done steps
    parser = OptionParser()
    parser.add_option("-s", "--steps", dest="steps",
                      help="use forward to use existing files as step indicator", metavar="int")

    (options, args) = parser.parse_args()

    if options.steps:
        if options.steps == "forward":
            steps = len((glob.glob('{}/*.npy*'.format(path))))
        elif not options.steps == "forward":
            steps = int(options.steps)
    elif not options.steps:
        steps = len((glob.glob('{}/*.npy*'.format(path))))

    print(steps)


    paused = False

    last_time = time.time()
    while True:

        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))


        pressed_k = get_keys.get_pressed_keys()
        tr_data.append([printscreen, pressed_k])
        img = None

        if save_steps < len(tr_data):
            steps += 1
            print('Writing.. | Step: ', steps)
            np.save(path+'data'+str(steps)+'.npy', tr_data)
            tr_data = []

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    print('Saving data')
    print('Path:', path)

    print('----------------')
    print('Finally Saved | Step: ', steps)
    print('----------------')

if __name__ == "__main__":
    main()
