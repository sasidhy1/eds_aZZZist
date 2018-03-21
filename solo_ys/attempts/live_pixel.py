import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(-1)
# print("video format: ", cap.shape)

start_time = time.time()
counter = 0;


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
		# create a mask
		mask = np.zeros(frame.shape[:2], np.uint8)
		mask[160:320, 210:426] = 255
		masked_img = cv2.bitwise_and(frame,frame,mask = mask)

		rev, temp = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)

		# Calculate histogram with mask and without mask
		# Check third argument for mask
		hist_full = cv2.calcHist([frame],[0],None,[256],[0,256])
		hist_mask = cv2.calcHist([frame],[0],mask,[256],[0,256])

		# cv2.imshow('orig',frame)
		# cv2.imshow('mask2',masked_img)
		# cv2.imshow('mask3',hist_full)
		# cv2.imshow('mask4',hist_mask)
		y = hist_mask * 3;
		cv2.putText(img = frame,
					text = 'Thresh: {}'.format(y[0]),
					org = (20,20),
					fontFace = cv2.FONT_HERSHEY_DUPLEX,
					fontScale = 0.5,
					color = (0, 255, 0))
		cv2.imshow("Edges", np.hstack([frame, masked_img, temp]))

		# plt.imshow(hist_mask,interpolation = 'nearest')
		# print(y);

		# if (x*3) <= 0:
		# 	print('BLINK');

		elapsed_time = time.time() - start_time
		time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
		# print(elapsed_time);

		# exit protocol
		if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
    else:
		break

cap.release()
cv2.destroyAllWindows()