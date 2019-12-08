# bufferlesscapture_sample001

This is a sample of bufferless capture.

I am referring to [this page](https://stackoverflow.com/questions/43665208/how-to-get-the-latest-frame-from-capture-device-camera-in-opencv-python).

Copy camera_uvc.py to the Lib folder.

Try the following.

```
from camera_uvc import *

cam1 = BufferlessCapture()
cam1.view()
cam1.release()

cam2 = NormalCapture()
cam2.view()
cam2.release()
```
