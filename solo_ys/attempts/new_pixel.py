import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(-1)
# print("video format: ", cap.shape)

start_time = time.time()
counter = 0;


while(cap.isOpened()):
    ret, frame = cap.read(0)
    if ret==True:

		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# create a mask
		rev, temp = cv2.threshold(frame, 70, 255, cv2.THRESH_BINARY)
		
		mask = np.zeros(temp.shape[:2], np.uint8)
		mask[160:320, 210:426] = 255
		masked_img = cv2.bitwise_and(temp,temp,mask = mask)

		lis = masked_img.flatten()
		pixels = lis[-1]
		print(pixels)
		# .convert('L')
		# pixels = np.array(im.getdata())          # get the pixels as a flattened sequence
		# lis = list(im.getdata())
		# print(lis)

		# black_thresh = 200
		# nblack = 0
		# for pixel in pixels:
		#     if pixel < black_thresh:
		#         nblack += 1
		# n = len(pixels)

		# if (nblack / float(n)) > 0.5:
		#     print("blink")		

		# Calculate histogram with mask and without mask
		# Check third argument for mask
		hist_full = cv2.calcHist([temp],[0],None,[256],[0,256])
		hist_mask = cv2.calcHist([temp],[0],mask,[256],[0,256])

		# cv2.imshow('orig',frame)
		# cv2.imshow('mask2',masked_img)
		# cv2.imshow('mask3',hist_full)
		# cv2.imshow('mask4',hist_mask)
		# y = hist_mask * 3;

		# if y[0] <= 0:
			# counter = counter + 1

		cv2.putText(img = frame,
					text = 'Blinks: {}'.format(counter),
					org = (20,20),
					fontFace = cv2.FONT_HERSHEY_DUPLEX,
					fontScale = 0.5,
					color = (0, 255, 0))
		cv2.imshow("Edges", np.hstack([frame, masked_img, temp]))

		# plt.imshow(hist_mask,interpolation = 'nearest')
		# print(y);

		# if (x*3) <= 0:
		# 	print('BLINK');

		# elapsed_time = time.time() - start_time
		# time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
		# print(elapsed_time);

		# exit protocol
		if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
    else:
		break

cap.release()
cv2.destroyAllWindows()