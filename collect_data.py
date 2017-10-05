import numpy as np
import cv2
import sys
import glob

from optparse import OptionParser
from hardw import get_keys
from screen import screen_cap

def main():

    #where file is stored
    path = 'D:/data_ai_ll/'

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

    while True:
        itr += 1
        pressed_k = get_keys.get_pressed_keys()
        img = screen_cap.grab_frame(size)
        tr_data.append([img, pressed_k])
        img = None

        if save_steps < len(tr_data):
            steps += 1
            print('Writing.. | Step: ', steps)
            np.save(path+'data'+str(steps)+'.npy', tr_data)
            tr_data = []

        if cv2.waitKey(1) & 0xFF == ord('q') or get_keys.get_stop_key('P'):
            break

    print('Saving data')
    print('Path:', path)

    print('----------------')
    print('Finally Saved | Step: ', steps)
    print('----------------')

if __name__ == "__main__":
    main()
