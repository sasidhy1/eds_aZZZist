import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
 
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
 
    # return the edged image
    return edged

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/reading.mp4')

boundaries = [
    ([0, 0, 0], [0, 0, 0]),
]

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    frame = frame[100:360, 300:640]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    diff = clahe.apply(v)

    edges = cv2.Canny(diff,200,250)


    lower_red = np.array(0)
    upper_red = np.array(20)

    mask = cv2.inRange(diff, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
 
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
 
    # apply Canny edge detection using a wide threshold, tight
    # threshold, and automatically determined threshold
    auto = auto_canny(blurred)

    contours =  cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        cv2.drawContours(edges, [c], -1, (0,225,0), 1)
        cv2.fillPoly(auto, pts =[c], color=(255,255,255))

    # Display the resulting frame
    # cv2.imshow("gray", np.hstack([hsv]))
    cv2.imshow("yes",diff)
    cv2.imshow("well",auto)
    # cv2.imshow("images", np.hstack([th1, th2, th3]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()