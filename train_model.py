import numpy as np
import glob
import time
import os


from model import cnn_model
from data import data_prog
from tqdm import tqdm

WIDTH = 480
HEIGHT = 270
LR = 0.001
#2best 0.00025 < 200gb
#1best 0.001 <200gb
EPOCHS = 20000

MODEL_NAME = 'Pete_vmtr'
#model_data/Pete_vmtr/
MODEL_TRAIN = 'model_data/Pete_vmtr/'

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
            data_train = np.load(f)
            file_step += 1

            batch_x = np.array([i[0] for i in data_train]).reshape(-1,WIDTH,HEIGHT,3)

            batch_y = [i[1] for i in data_train]


            model.fit({'input': batch_x}, {'targets': batch_y}, n_epoch=1, snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

            #releasing data from memory
            data = None
            batch_x = None
            batch_y = None
            
            if(file_step%10 == 0):
                print('###################-Model-Saved-###################')
                print('Abs. ep: ', e)
                model.save('model_data/'+MODEL_NAME)

    print('###################-Finished-Learning-###################')
    model.save('model_data/'+MODEL_NAME)



if __name__ == "__main__":
    main()
