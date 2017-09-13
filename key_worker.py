import threading
from time import sleep
import keyboard as kb

class drive_worker(threading.Thread):

    #f: forwad
    #fr: forwad_right
    #fl: forwad_left
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
        while True:
            if(self.steering_acc=="stop"):
                drive_worker.stop()
            elif(self.steering_acc=="forwad"):
                drive_worker.forwad()
            elif(self.steering_acc=="forwad_right"):
                drive_worker.forwad_right()
            elif(self.steering_acc=="forwad_left"):
                drive_worker.forwad_left()
            elif(self.steering_acc=="backwards"):
                drive_worker.backwards()
            elif(self.steering_acc=="backwards_right"):
                drive_worker.backwards_right()
            elif(self.steering_acc=="backwards_left"):
                drive_worker.backwards_left()

    def forwad():
        kb.press('w')


    def forwad_right():
        kb.press('w')
        kb.press('d')


    def forwad_left():
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

    def stop():
        print('stop')
