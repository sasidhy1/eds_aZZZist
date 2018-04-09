import numpy as np
import cv2

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/front.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(33,33),0)
    blur = cv2.bilateralFilter(blur,9,75,75)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(frame,markers)
    frame[markers == -1] = [255,0,0] 

    contours =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[-2]
    for c in contours:
        cv2.drawContours(blur, [c], -1, (0,255,0), 3)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('thresh',thresh)
    cv2.imshow('blur',blur)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()