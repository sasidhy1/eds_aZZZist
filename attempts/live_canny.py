import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import glob

def auto_canny(video, sigma=.33):
	# compute the median of the single channel pixel intensities
	v = np.median(video)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(video, lower, upper)
 
	# return the edged video
	return edged

cap = cv2.VideoCapture(-1)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret==True:
		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (3, 3), 0)

		# apply Canny edge detection using a wide threshold, tight
		# threshold, and automatically determined threshold
		wide = cv2.Canny(blurred, 10, 200)
		tight = cv2.Canny(blurred, 225, 250)
		auto = auto_canny(blurred)

		# show the video
		cv2.imshow("Original", frame)
		cv2.imshow("Edges", np.hstack([wide, tight, auto]))

		# exit protocol
		if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
    else:
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()