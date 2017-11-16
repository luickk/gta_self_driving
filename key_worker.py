import threading
from time import sleep
from hardw import get_keys
import keyboard as kb


class drive_worker(threading.Thread):

    #f: forward
    #fr: forward_right
    #fl: forward_left
    #
    #b: backwards
    #br: backwards_right
    #bl: backwards_left
    steering_acc="stop"

    def __init__(self):
        super(drive_worker, self).__init__()
        self.daemon = True
        self.start()
        self.steering_acc="stop"

    def run(self):
        paused = False
        while True:
            print('loop_kw')
            sleep(0.5)
            if get_keys.get_pause_key():
                paused = True
            elif not get_keys.get_pause_key():
                paused = False
            if paused:
                if(self.steering_acc=="forward"):
                    drive_worker.release_all()
                    drive_worker.forward()
                elif(self.steering_acc=="forward_right"):
                    drive_worker.release_all()
                    drive_worker.forward_right()
                elif(self.steering_acc=="forward_left"):
                    drive_worker.release_all()
                    drive_worker.forward_left()
                elif(self.steering_acc=="backwards"):
                    drive_worker.release_all()
                    drive_worker.backwards()
                elif(self.steering_acc=="backwards_right"):
                    drive_worker.release_all()
                    drive_worker.backwards_right()
                elif(self.steering_acc=="backwards_left"):
                    drive_worker.release_all()
                    drive_worker.backwards_left()

    def forward():
        kb.press('w')


    def forward_right():
        kb.press('w')
        kb.press('d')


    def forward_left():
        kb.press('w')
        kb.press('a')


    def backwards():
        kb.press('s')


    def backwards_right():
        kb.press('s')
        kb.press('d')


    def backwards_left():
        kb.press('s')
        kb.press('a')

    def release_all():
        kb.release('w')
        kb.release('a')
        kb.release('s')
        kb.release('d')
