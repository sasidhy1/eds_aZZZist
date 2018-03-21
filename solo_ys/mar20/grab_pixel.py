import numpy as np
import cv2
import scipy
from scipy import ndimage
import argparse
import datetime
import imutils
import time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
 
cap = cv2.VideoCapture('dark2-2.mp4')
blur_radius = (20,20)
# threshold = 50

# define the list of boundaries
boundaries = [
	([68, 86, 163], [255, 255, 255]),
]

percent = None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.blur(frame, blur_radius)

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

    amt = float(cv2.countNonZero(mask))
    total = float(640 * 480)
    percent = round((amt / total * 100),2)

    cv2.putText(img = output,
            text = 'amount: {}%'.format(percent),
            org = (20,20),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.5,
            color = (0, 255, 0))

    # Display the resulting frame
    cv2.imshow("images", np.hstack([frame, output]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()