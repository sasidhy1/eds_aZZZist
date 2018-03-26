import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time
from PIL import Image


cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/study.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    frame = frame[100:360, 300:640]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4,4))
    diff = clahe.apply(v)
    blur = cv2.bilateralFilter(diff,9,75,75)
    edges = cv2.Canny(blur,250,300)

    # (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(diff)
    # cv2.circle(diff, minLoc, 25, (255, 0, 0), 2)

    contours =  cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        if cv2.contourArea(c) > 5:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.drawContours(gray, [c], -1, (0, 255, 0), 2)
            cv2.circle(gray, (cX, cY), 7, (0, 0, 0), -1)

    # mask = cv2.inRange(diff, 0, 10)
    # output = cv2.bitwise_not(diff, diff, mask = mask)


    # Display the resulting frame
    cv2.imshow("gray", np.hstack([gray,edges]))
    # cv2.imshow("gray", np.hstack([hsv]))

    # cv2.imshow("images", np.hstack([th1, th2, th3]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()