import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/sleep.mp4')
# blur_radius = (20,20)
# threshold = 50

# define the list of boundaries
boundaries = [
    ([250, 250, 250], [255, 255, 255]),
]

# percent = None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    frame = frame[100:360, 300:640]

    # r = frame[:,:,1];
    # b = frame[:,:,2];
    # g = frame[:,:,3];
    
    # mask = r == 255 & g == 255 & b = 255

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.blur(frame, blur_radius)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # labeled, nr_objects = ndimage.label(smooth > threshold)
    # flip = cv2.flip(smooth,1)

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
 
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask = mask)

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.blur(frame, blur_radius)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(frame, maxLoc, 25, (255, 0, 0), 2)

    # amt = float(cv2.countNonZero(mask))
    # total = float(640 * 480)
    # percent = round((amt / total * 100),2)

    # cv2.putText(img = output,
    #         text = 'amount: {}%'.format(percent),
    #         org = (20,20),
    #         fontFace = cv2.FONT_HERSHEY_DUPLEX,
    #         fontScale = 0.5,
    #         color = (0, 255, 0))

    # Display the resulting frame
    cv2.imshow("images", np.hstack([frame, output]))
    # cv2.imshow("gray", gray)
    # cv2.imshow("gray", mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()