# bufferlesscapture_sample001

This is a sample of bufferless capture.

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
