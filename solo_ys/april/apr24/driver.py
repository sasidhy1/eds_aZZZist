# import the necessary packages
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2
import numpy as np

death = 0.0
temp = 0
counter = 0

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
 
# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

start_time = time.time()

while(True):
    elapsed_time = time.time() - start_time
    elap = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    onset = time.time()

    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
 
    # draw the timestamp on the frame
    timestamp = datetime.datetime.now()
    # ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    # cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		# 0.35, (0, 0, 255), 1)
    
    roi = frame[100:300, 100:250]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret, thresh_img = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4,4))
    hist = clahe.apply(gray)
    blur = cv2.bilateralFilter(hist,9,75,75)
    edges = cv2.Canny(blur,150,220)

    status = "eyes closed"

    contours1 =  cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours1:
        if cv2.contourArea(c) > 13:
            status = "eyes OPEN"
            death = time.time()
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.drawContours(gray, [c], -1, 0, 2)
            cv2.circle(gray, (cX, cY), 7, 0, -1)

            contours2 =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
            for c in contours2:
                cv2.drawContours(roi, [c], -1, (255,255,255), -1)

    new = roi[0:360-70, 0:640-360]

    cv2.putText(img = frame,
        text = 'elapsed time: {}'.format(elap),
        org = (10,20),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 0.5,
        color = (0, 255, 0))

    cv2.putText(img = frame,
        text = 'user has fallen asleep {} times'.format(counter),
        org = (10,80),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 0.5,
        color = (0, 255, 0))

    cv2.putText(img = frame,
        text = 'status: {}'.format(status),
        org = (10,40),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 0.5,
        color = (0, 255, 0))

    wake = onset - death

    if wake > 1:
        cv2.putText(img = frame,
            text = 'subject is ASLEEP',
            org = (10,60),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.5,
            color = (0, 0, 255))
        temp += 1

    else:
        cv2.putText(img = frame,
            text = 'subject is awake',
            org = (10,60),                                                  
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.5,
            color = (0, 255, 0))
        if temp != 0:
            counter += 1
        temp = 0

    cv2.imshow("disp1", frame)
    # cv2.imshow("disp", gray)
    # cv2.imshow("disp2", roi)
    # cv2.imshow("disp3", new)
    cv2.imshow("images", np.hstack([edges, gray]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()