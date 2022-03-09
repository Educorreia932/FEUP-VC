import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    # Taking each frame of the video
    ret, frame = video.read()

    # Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image for red values
    mask = cv2.inRange(hsv, (175, 170, 20), (180, 255, 255))
    result = cv2.bitwise_and(hsv, hsv, mask=mask)

    cv2.imshow("Video capture", cv2.cvtColor(result, cv2.COLOR_HSV2BGR))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
