# -*- coding: utf-8 -*-

import time
import threading
import queue
import cv2

class BufferlessCapture:
    # Initialize
    def __init__(self, id=0, width=640, height=480, exposure=-6):
        self.cap = cv2.VideoCapture(id)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
        print('--------------------')
        print('BufferlessCapture.__init__')
        print('--------------------')
        print('Width = {0}'.format(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        print('Height = {0}'.format(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print('Exposure = {0}'.format(self.cap.get(cv2.CAP_PROP_EXPOSURE)))
        print('')
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()
    # Read frames as soon as they are available, keeping only most recent one.
    def _reader(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait() #discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)
    # Read
    def read(self):
        return self.q.get()
    # Release
    def release(self):
        self.cap.release()
    # View
    # Close with ESC.
    def view(self, delay=1):
        k = 0
        while k != 27:
            img = self.grab()
            cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
            cv2.imshow("img", img)
            k = cv2.waitKey(delay)
        cv2.destroyAllWindows()

class NormalCapture:
    # Initialize
    def __init__(self, id=0, width=640, height=480, exposure=-6):
        self.cap = cv2.VideoCapture(id)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
        print('--------------------')
        print('BufferlessCapture.__init__')
        print('--------------------')
        print('Width = {0}'.format(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        print('Height = {0}'.format(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print('Exposure = {0}'.format(self.cap.get(cv2.CAP_PROP_EXPOSURE)))
        print('')
    # Read
    def read(self):
        ret, img = self.cap.read()
        return img
    # Release
    def release(self):
        self.cap.release()
    # View
    # Close with ESC.
    def view(self, delay=1):
        k = 0
        while k != 27:
            ret, img = self.cap.read()
            cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
            cv2.imshow("img", img)
            k = cv2.waitKey(delay)
        cv2.destroyAllWindows()