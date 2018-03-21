import numpy as np
import cv2
import scipy
from scipy import ndimage
import datetime
import imutils
import time

class BackGroundSubtractor:
    def __init__(self,alpha,firstFrame):
        self.alpha  = alpha
        self.backGroundModel = firstFrame

    def getForeground(self,frame):
        self.backGroundModel =  frame * self.alpha + self.backGroundModel * (1 - self.alpha)

        return cv2.absdiff(self.backGroundModel.astype(np.uint8),frame)

cap = cv2.VideoCapture('dark2-2.mp4')
# blur_radius = (10,10)
# threshold = 50

def denoise(frame):
    frame = cv2.medianBlur(frame,5)
    frame = cv2.GaussianBlur(frame,(5,5),0)
    return frame

percent = None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))

    backSubtractor = BackGroundSubtractor(0.01,denoise(frame))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.blur(frame, blur_radius)

    # labeled, nr_objects = ndimage.label(smooth > threshold)
    # flip = cv2.flip(smooth,1)

    # Display the resulting frame
    cv2.imshow("orig", frame)
    cv2.imshow("filter", denoise(frame))

    fg = backSubtractor.getForeground(denoise(frame))
    ret, mask = cv2.threshold(fg, 15, 255, cv2.THRESH_BINARY)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()