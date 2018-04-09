import numpy as np
import cv2

cap1 = cv2.imread('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/open.png')
cap2 = cv2.imread('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/closed.png')

# Our operations on the frame come here
gray = cv2.cvtColor(cap1, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret, thresh_img = cv2.threshold(blur,50,255,cv2.THRESH_BINARY)

contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
for c in contours:
    cv2.drawContours(cap1, [c], -1, (0,255,0), 3)

# Display the resulting frame
cv2.imshow('frame',cap1)
cv2.waitKey(0)

# When everything done, release the capture
cv2.destroyAllWindows()