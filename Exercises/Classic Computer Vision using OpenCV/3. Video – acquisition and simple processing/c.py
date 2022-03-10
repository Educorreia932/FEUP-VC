import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    black_and_white = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]
  
    cv2.imshow("Video capture", frame)
    cv2.imshow("Black and white", black_and_white)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
video.release()
cv2.destroyAllWindows()

cv2.imwrite("Images/3-1.jpg", frame)
cv2.imwrite("Images/3-2.jpg", black_and_white)

