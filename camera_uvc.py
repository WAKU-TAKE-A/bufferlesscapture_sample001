# -*- coding: utf-8 -*-

import time
import threading
import queue
import cv2

class BufferlessCapture:
    """
    Get the latest frame from capture device (camera).
    """
    def __init__(self, id=0, width=640, height=480, exposure=-6):
        """
        Initialize
        """
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
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()
    def _reader(self):
        """
        Read frames as soon as they are available, keeping only most recent one.
        """
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
    def read(self):
        """
        Read
        """
        return self.q.get()
    def release(self):
        """
        Release
        """
        self.cap.release()
    def view(self, delay=1):
        """
        View

        * Close with ESC.
        """
        k = 0
        while k != 27:
            ret, img = self.cap.read()
            cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
            cv2.imshow("img", img)
            k = cv2.waitKey(delay)
        cv2.destroyAllWindows()

class NormalCapture:
    """
    Get the frame from the capture device (camera) Ordinarily.
    """
    def __init__(self, id=0, width=640, height=480, exposure=-6):
        """
        Initialize
        """
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
    def read(self):
        """
        Read
        """
        ret, img = self.cap.read()
        return img
    def release(self):
        """
        Release
        """
        self.cap.release()
    def view(self, delay=1):
        """
        View

        * Close with ESC.
        """
        k = 0
        while k != 27:
            ret, img = self.cap.read()
            cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
            cv2.imshow("img", img)
            k = cv2.waitKey(delay)
        cv2.destroyAllWindows()

