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

def is_contour_bad(c):
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# the contour is 'bad' if it is not a rectangle
	return not len(approx) == 4

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

		# find contours in the image and initialize the mask that will be
		# used to remove the bad contours
		(_, cnts, _) = cv2.findContours(auto.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		mask = np.ones(frame.shape[:2], dtype="uint8") * 255

		# loop over the contours
		for c in cnts:
			# if the contour is bad, draw it on the mask
			if is_contour_bad(c):
				cv2.drawContours(mask, [c], -1, 0, -1)		

		# remove the contours from the image and show the resulting images
		frame = cv2.bitwise_and(frame, frame, mask=mask)
		cv2.imshow("Mask", mask)
		cv2.imshow("After", frame)

		# show the video
		# cv2.imshow("Original", frame)
		# cv2.imshow("Edges", np.hstack([wide, tight, auto]))

		# exit protocol
		if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
    else:
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()