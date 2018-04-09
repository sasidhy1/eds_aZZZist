import numpy as np
import cv2

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/reading.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    frame = frame[100:360, 300:640]

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh_img = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    
    contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        cv2.drawContours(gray, [c], -1, (255,0,0), 1)
        # (x, y, w, h) = cv2.boundingRect(c)
        # cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), -1)
        cv2.fillPoly(gray, pts =[c], color=(0,0,0))

    # ret, thresh_img = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    
    # contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    # for c in contours:
    #     cv2.drawContours(gray, [c], -1, (255,0,0), 1)
    #     cv2.fillPoly(gray, pts =[c], color=(255,255,255))

    # Display the resulting frame
    cv2.imshow('blur',gray)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
