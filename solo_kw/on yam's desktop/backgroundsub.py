import numpy as np
import cv2

cap = cv2.VideoCapture('take1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(int history = 200, double varThrshold = 16, bool detectShadows = true)

print ("working")

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()