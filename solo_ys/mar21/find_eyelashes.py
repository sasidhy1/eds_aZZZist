import colorsys
import numpy as np
import cv2

cap = cv2.VideoCapture('/home/sasidhy1/Desktop/eds_azzzist/SAMPLES/IR_reading_light.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,360))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret, thresh_img = cv2.threshold(blur,91,255,cv2.THRESH_BINARY)

    
    
    # contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    # for c in contours:
        # cv2.drawContours(frame, [c], -1, (0,255,0), 3)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# apply a Gaussian blur to the image then find the brightest
# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)
# cv2.circle(cap, maxLoc, 60, (255, 0, 0), 2)

# agg = colorsys.rgb_to_hsv(250,250,250)
# print(agg)

# Display the resulting frame
# cv2.imshow('frame',cap)
# cv2.waitKey(0)

# When everything done, release the capture
# cv2.destroyAllWindows()