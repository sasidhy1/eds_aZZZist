import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(-1)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('/home/sasidhy1/Videos/canny1.avi',fourcc, 30, (640,480), True)
out2 = cv2.VideoWriter('/home/sasidhy1/Videos/canny2.avi',fourcc, 30, (640,480), False)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret==True:
		# Our operations on the frame come here
		canny = cv2.Canny(frame,100,200)

		# write the frame 
		out1.write(frame)
		out2.write(canny)

		# Display the resulting frame
		cv2.imshow('stream',frame)
		cv2.imshow('edge stream',canny)

		# exit protocol
		if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
    else:
		break

# When everything done, release the capture
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()