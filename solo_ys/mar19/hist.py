import numpy as np
import cv2
import scipy
from scipy import ndimage

cap = cv2.VideoCapture('/home/sasidhy1/Videos/samples/take1.mp4')
fgbg = cv2.BackgroundSubtractorMOG2()
blur_radius = 5.0
threshold = 50

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    frame = cv2.resize(frame,(640,480))
    fgmask = cv2.resize(fgmask,(640,480))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smooth = ndimage.gaussian_filter(gray, blur_radius)

    labeled, nr_objects = ndimage.label(smooth > threshold)
    flip = cv2.flip(smooth,1)

    cv2.putText(img = flip,
            text = 'objects: {}'.format(nr_objects),
            org = (20,20),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.5,
            color = (0, 255, 0))

    # Display the resulting frame
    cv2.imshow("stacked", frame)
    cv2.imshow("macked", fgmask)
    # cv2.imshow("stacked", np.hstack([frame, fgmask]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()