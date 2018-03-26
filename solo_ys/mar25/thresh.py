import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/reading.mp4')
# blur_radius = (20,20)
# threshold = 50

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    frame = frame[100:360, 300:640]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    diff = clahe.apply(v)

    # # global thresholding
    ret1,th1 = cv2.threshold(diff,200,255,cv2.THRESH_BINARY)

    # # # Otsu's thresholding
    ret2,th2 = cv2.threshold(diff,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # # # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(diff,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.blur(frame, blur_radius)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # labeled, nr_objects = ndimage.label(smooth > threshold)
    # flip = cv2.flip(smooth,1)

    # Display the resulting frame
    cv2.imshow("gray", np.hstack([hsv]))
    cv2.imshow("yes",diff)
    # cv2.imshow("images", np.hstack([th1, th2, th3]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()