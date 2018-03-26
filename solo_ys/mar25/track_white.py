import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/ambient.mp4')
# blur_radius = (20,20)
# threshold = 50

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    frame = frame[0:360, 300:640]

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.blur(frame, blur_radius)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(frame, maxLoc, 25, (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow("images", np.hstack([frame]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()