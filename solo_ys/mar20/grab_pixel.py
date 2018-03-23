import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/IR_sleep_light.mp4')
blur_radius = (20,20)
# threshold = 50

# define the list of boundaries
boundaries1 = [
    ([68, 86, 163], [255, 255, 255]),
]

# define the list of boundaries
boundaries2 = [
    ([0, 0, 0], [50, 50, 50]),
]

percent = None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.blur(frame, blur_radius)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # labeled, nr_objects = ndimage.label(smooth > threshold)
    # flip = cv2.flip(smooth,1)

    # loop over the boundaries
    for (lower, upper) in boundaries1:
        # create NumPy arrays from the boundaries
        lower1 = np.array(lower, dtype = "uint8")
        upper1 = np.array(upper, dtype = "uint8")
 
        # find the colors within the specified boundaries and apply
        # the mask
        mask1 = cv2.inRange(frame, lower1, upper1)
        output1 = cv2.bitwise_and(frame, frame, mask = mask1)

    for (lower, upper) in boundaries2:
        # create NumPy arrays from the boundaries
        lower2 = np.array(lower, dtype = "uint8")
        upper2 = np.array(upper, dtype = "uint8")
 
        # find the colors within the specified boundaries and apply
        # the mask
        mask2 = cv2.inRange(frame, lower2, upper2)
        output2 = cv2.bitwise_and(frame, frame, mask = mask2)

        # (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(output2)
        # cv2.circle(frame, minLoc, 60, (255, 0, 0), 2)

    amt = float(cv2.countNonZero(mask1))
    total = float(640 * 480)
    percent = round((amt / total * 100),2)

    cv2.putText(img = output1,
            text = 'amount: {}%'.format(percent),
            org = (20,20),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.5,
            color = (0, 255, 0))

    output = cv2.add(output1,output2)

    # Display the resulting frame
    cv2.imshow("images", np.hstack([frame, output]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()