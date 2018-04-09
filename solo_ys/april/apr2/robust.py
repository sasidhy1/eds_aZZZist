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
cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/study.mp4')
# cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/reading.mp4')

first_iter = True
result = None

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    
    # roi = frame[70:360, 300:640]

    if first_iter:
        avg = np.float32(frame)
        first_iter = False

    cv2.accumulateWeighted(frame, avg, 0.005)
    result = cv2.convertScaleAbs(avg)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh_img = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4,4))
    hist = clahe.apply(gray)
    blur = cv2.bilateralFilter(hist,9,75,75)
    edges = cv2.Canny(blur,50,80)

    contours1 =  cv2.findContours(hist,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours1:
        cv2.drawContours(gray, [c], -1, 0, 2)

    # conn = cv2.connectedComponents(edges,4)

        # if cv2.contourArea(c) > 9:
        #     status = "eyes OPEN"
        #     M = cv2.moments(c)
        #     cX = int(M["m10"] / M["m00"])
        #     cY = int(M["m01"] / M["m00"])

        #     cv2.drawContours(gray, [c], -1, 0, 2)
        #     cv2.circle(gray, (cX, cY), 7, 0, -1)

        #     contours2 =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
        #     for c in contours2:
        #         cv2.drawContours(frame, [c], -1, (255,255,255), -1)

    # new = roi[cY:360-70, 0:640-360]

    # temp = cv2.bitwise_and(frame,result)
    # temp = cv2.bitwise_or(frame,result)
    # temp = cv2.bitwise_not(frame,result)
    # temp = cv2.bitwise_xor(frame,result)

    cv2.imshow("temp", gray)
    # cv2.imshow("disp1", frame)
    # cv2.imshow("disp", gray)
    # cv2.imshow("disp2", roi)
    # cv2.imshow("disp3", new)
    # cv2.imshow("images", np.hstack([edges, gray]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()