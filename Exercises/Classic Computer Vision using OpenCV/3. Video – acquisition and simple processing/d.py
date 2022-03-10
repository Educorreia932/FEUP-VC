import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    # Taking each frame of the video
    ret, frame = video.read()

    # Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image for red values
    mask_1 = cv2.inRange(hsv, (170, 170, 20), (180, 255, 255))
    mask_2 = cv2.inRange(hsv, (0, 200, 20), (10, 255, 255))

    mask = mask_1 | mask_2
    result = cv2.bitwise_and(hsv, hsv, mask=mask)
    masked = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

    cv2.imshow("Video capture", masked)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

cv2.imwrite("Images/4.jpg", masked)
