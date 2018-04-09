import numpy as np
import cv2

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/front.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray,(33,33),0)
    bilat = cv2.bilateralFilter(gauss,9,75,75)

    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4,4))
    hist = clahe.apply(bilat)

    ret, thresh = cv2.threshold(hist,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    edges = cv2.Canny(hist,40,50)

    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(hist,kernel,iterations = 1)

    contours =  cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[-2]
    for c in contours:
        if cv2.contourArea(c) > 10:
            cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            

    # Display the resulting frame
    cv2.imshow('temp',hist)
    # cv2.imshow('hist',hist)
    # cv2.imshow('frame',frame)
    # cv2.imshow('thresh',thresh)
    # cv2.imshow('blur',bilat)
    # cv2.imshow('edges',edges)
    # cv2.imshow('dil',dilation)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()