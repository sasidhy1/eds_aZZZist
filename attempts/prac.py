import cv2 
#Program to capture a video from the default 
#camera (0) and display it live on the screen 
cap = cv2.VideoCapture(0) 
while(True): 
    # Capture frame-by-frame 
    [retval, frame] = cap.read()    
    # Display the resulting frame 
    cv2.imshow('frame',frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
# When everything done, release the capture 
cap.release() 
cv2.destroyAllWindows()
