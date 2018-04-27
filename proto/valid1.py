# import necessary packages
from pivideostream import PiVideoStream
import cv2
import imutils
import numpy as np
import datetime
import time

# initialize variables
microsleep = False          # boolean to store subject state, default
counter = 0                 # variable to count instances of microsleep

# initialize the video stream specs, allow time for camera sensor to warmup
vs = PiVideoStream(resolution=(320, 240),framerate=32)
vs.start()
time.sleep(2.0)

# initialize start time after warmup
start_time = time.time()

while(True):
    frame = vs.read()                                               # start parsing through frames
    frame = imutils.resize(frame, width=400)                        # resize each individual frames

    onset = time.time()                                             # declare time of EC onset
    
    roi = frame[100:300, 100:250]                                   # crop to region of interest
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)                    # convert BGR frame to grayscale
    ret, thresh_img = cv2.threshold(gray,200,255,cv2.THRESH_BINARY) # create binary (BW) mask of grayscale image

    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4,4))      # perform adaptive histogram equalization
    hist = clahe.apply(gray)                                        # apply histogram to grayscale frame
    blur = cv2.bilateralFilter(hist,9,75,75)                        # noise removal, keep edges intact
    edges = cv2.Canny(blur,150,220)                                 # apply canny edge detection algorithm

    status = "eyes closed"                                          # declare current status, default is closed


    # detect contours within canny edge result, only display contours above predefined area threshold
    # calculate centerpoints of each contour moment, display with black circle on grayscale frame
    # this achieves accurate segmentation the eyelid and eyelashes, and extracts x,y-position data
    contours =  cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        if cv2.contourArea(c) > 13:

            end = time.time()       # declare time of EC end
            status = "eyes OPEN"    # declare current status, eyes open

            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.drawContours(gray, [c], -1, 0, 2)
            cv2.circle(gray, (cX, cY), 7, 0, -1)

            # contours calculated from binary mask when eyelid folds and eyelashes are detected
            # each contiguous contour filled with white for visualizing sclera segmentation
            sclera =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
            for s in sclera:
                cv2.drawContours(roi, [s], -1, (255,255,255), -1)

    # visualize dynamic cropping based on calculated canny edge contours
    new = roi[cY:360-70, 0:640-360]

    # calculate elapsed time for display
    # convert time format for readability
    elapsed_time = time.time() - start_time
    elap = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    # display elapsed time on frame
    cv2.putText(img = frame,
        text = 'elapsed time: {}'.format(elap),
        org = (10,20),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 0.45,
        color = (0, 255, 0))

    # draw the timestamp on the frame
    timestamp = datetime.datetime.now()
    ts = timestamp.s trftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(img = frame,
        text = '{}'.format(ts),
        org = (10, frame.shape[0] - 10),
        fontFace = cv2.FONT_HERSHEY_SIMPLEX,
        fontScale = 0.45,
        color = (0, 0, 255) )

    # display eye status on frame
    cv2.putText(img = frame,
        text = 'status: {}'.format(status),
        org = (10,40),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 0.45,
        color = (0, 255, 0))

    cv2.putText(img = frame,
        text = 'user has fallen asleep {} times'.format(counter),
        org = (10,80),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 0.45,
        color = (0, 255, 0))

    # calculate duration of EC
    wake = onset - end

    # display subject status on frame
    # microsleep detected, EC > 1000ms
    if wake > 1:
        cv2.putText(img = frame,
            text = 'subject is ASLEEP',
            org = (10,60),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.45,
            color = (0, 0, 255))
        microsleep = True

    # display subject status on frame
    # NO microsleep detected, EC <= 1000ms
    else:
        cv2.putText(img = frame,
            text = 'subject is awake',
            org = (10,60),                                                  
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.45,
            color = (0, 255, 0))
        if microsleep:
            counter += 1
            p = subprocess.Popen(["python", "verif_sound.py"], shell=False)
        microsleep = False
        
    cv2.imshow("disp1", frame)
    # cv2.imshow("disp", gray)
    # cv2.imshow("disp2", roi)
    # cv2.imshow("disp3", new)
    # cv2.imshow("images", np.hstack([edges, gray]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# do a bit of cleanup
p.kill()
cv2.destroyAllWindows()
vs.stop()