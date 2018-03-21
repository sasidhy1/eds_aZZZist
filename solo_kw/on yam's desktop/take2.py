import numpy as np
import cv2

RAW = "take1.mp4"

cap = cv2.VideoCapture(RAW)
first_iter = True
back = None
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    if first_iter:
        avg = np.float32(frame)
        first_iter = False

    cv2.accumulateWeighted(frame, avg, 0.005)
    back = cv2.convertScaleAbs(avg)

cv2.imshow("result.jpg", back)
cv2.imwrite("averaged_frame.jpg", back)
cv2.waitKey(0)

# sub = cv2.subtract(RAW,result)
# cv2.imshow("subtracted.mp4", )

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
