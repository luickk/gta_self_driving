import numpy as np
import glob
import time
import os

from model import cnn_model
from data import data_prog
from tqdm import tqdm

WIDTH = 480
HEIGHT = 270
LR = 0.000000001
EPOCHS = 20000

MODEL_NAME = 'Pete'
MODEL_TRAIN = 'model_data/Pete'

#training data path
path = 'D:/data_ai/'

def main():
    model = cnn_model.googlenet(WIDTH, HEIGHT, 3, LR, output=8, model_name=MODEL_NAME)


    if MODEL_TRAIN:
        model.load(MODEL_TRAIN)

    files = sorted(glob.glob('{}/*.npy*'.format(path)), key=data_prog.numericalSort)
    for e in tqdm(range(EPOCHS)):
        file_step = 0
        for f in files:
            time_start = time.time()
            data_train = np.load(f)
            file_step += 1
            #Y
            batch_y = data_prog.form_data_y(np.array([i[1] for i in data_train], dtype=object))

            #X
            batch_x = data_prog.form_data_x(np.array([i[0] for i in data_train], dtype=object)).reshape(-1,WIDTH,HEIGHT,3)

            model.fit({'input': batch_x}, {'targets': batch_y}, n_epoch=1, snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

            #releasing data from memory
            data = None
            batch_x = None
            batch_y = None
            time_end = time.time()
            print('Loop took: ', time_end - time_start)

            if(file_step%10 == 0):
                print('###################-Model-Saved-###################')
                print('Abs. ep: ', e)
                model.save('model_data/'+MODEL_NAME)

    print('###################-Finished-Learning-###################')
    model.save('model_data/'+MODEL_NAME)



if __name__ == "__main__":
    main()
