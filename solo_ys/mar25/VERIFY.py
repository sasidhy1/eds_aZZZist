import numpy as np
import cv2
import scipy
from scipy import ndimage
import datetime
import imutils
import time

# cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/ambient.mp4')
# cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/sleep.mp4')
# cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/relax.mp4')
# cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/study.mp4')
cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/reading.mp4')

cir = False

start_time = time.time()

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    roi = frame[70:360, 300:640]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret, thresh_img = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4,4))
    diff = clahe.apply(gray)
    blur = cv2.bilateralFilter(diff,9,75,75)
    edges = cv2.Canny(blur,250,300)

    contours =  cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        if cv2.contourArea(c) > 7:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.drawContours(gray, [c], -1, (0, 255, 0), 2)
            each = cv2.circle(gray, (cX, cY), 7, (0, 0, 0), -1)

    contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        cv2.drawContours(roi, [c], -1, (255,255,255), -1)
    
    cv2.line(roi,(0,cY+70),(640,cY+70),(255,0,0),5)
    cv2.rectangle(roi, (0,0), (640,cY+70), (0, 0, 0), -1)

    mask = cv2.inRange(gray, 250, 255)
    output = cv2.bitwise_and(gray, gray, mask = mask)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cir = cv2.circle(roi, maxLoc, 25, (255, 0, 255), 2)

    ## REPLACE WITH MASK

    # amt = float(cv2.countNonZero(mask))
    # total = float(640 * 480)
    # percent = round((amt / total * 100),2)

    elapsed_time = time.time() - start_time
    time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    # print(elapsed_time);

    if cir:
    	status = "pupil present"
    else:
        status = "searching..."	

    cv2.putText(img = roi,
            text = 'status: {}. \ntime elapsed: {}'.format(status,elapsed_time),
            org = (20,20),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.5,
            color = (0, 255, 0))

    cv2.imshow("disp", edges)
    cv2.imshow("disp1", frame)
    cv2.imshow("disp2", roi)
    cv2.imshow("disp3", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()