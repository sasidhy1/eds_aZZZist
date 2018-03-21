import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time

cap = cv2.VideoCapture(-1)
blur_radius = (20,20)
# threshold = 50

percent = None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(frame, blur_radius)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # output = 

    # Display the resulting frame
    cv2.imshow("images", np.hstack([frame, blur, hsv]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()