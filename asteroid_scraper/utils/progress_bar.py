# coding=utf-8
import sys
import threading
import time


class ProgressBarThread(threading.Thread):
    def __init__(self, delay=0.2):
        super(ProgressBarThread, self).__init__()
        self.delay = delay  # interval between updates
        self.running = False

    def start(self):
        self.running = True
        super(ProgressBarThread, self).start()

    def run(self):
        while self.running:
            for c in (u'◑', u'◒', u'◐', u'◓'):
                sys.stdout.write('\rScraping asteroids ' + c + c + c + c + c + c + c + c + c + c +
                                                         c + c + c + c + c + c + c + c + c + c)
                sys.stdout.flush()
                time.sleep(self.delay)

    def stop(self):
        self.running = False
        self.join()  # wait for run() method to terminate
        sys.stdout.write('\r         \r')  # clean-up
        sys.stdout.flush()
