opencvhandtracking
=======
![PyPI](https://img.shields.io/pypi/v/opencvhandtracking) [![Contributors](https://img.shields.io/badge/contributers-1-orange.svg?style=flat-square)](#contributors-) ![GitHub last commit](https://img.shields.io/github/last-commit/AlDevStuff/opencvhandtracking) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/AlDevStuff/opencvhandtracking) ![GitHub](https://img.shields.io/github/license/AlDevStuff/opencvhandtracking)



Library for OPENCV users. Easily implement hand tracking to your project without any manual work.


Features
--------

- Open camera instantly with sample code
- Track hands


Installation
------------
On your project directory, make sure to have virtual environment activated. This library will download both opencv and mediapipe. Run:
```sh
pip install opencvtracking
```


Usage
-----
Import the library:
```python
import cv2
from opencvtracking import HandGesture
```
To implement the library: 
```python
cap = cv2.VideoCapture()
handtrckingdetector = opencvhandtracking.HandGesture()

# This example is for the camera, but you can do this on anything from video to pictures.

while True:
    success, img = cap.read()
    img = handtrckingdetector.drawHand(img)
    landmarkList = handtrckingdetector.handPosition(img)
    
    # fps on the window [optional]
    cv2.imshow("Image", img)
    cv2.waitKey(1)
```

Contribute
----------

- Issue Tracker: https://github.com/AlDevStuff/opencvhandtracking/issues
- Source Code: https://github.com/AlDevStuff/opencvhandtracking

Pull requests welcome!


Support
-------

If you are having issues, please let me know.


License
-------

The project is licensed under the MIT license.