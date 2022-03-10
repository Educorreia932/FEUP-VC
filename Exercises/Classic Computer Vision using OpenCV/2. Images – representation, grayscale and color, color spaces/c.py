import cv2
import numpy as np

filename = "Images/lizard.jpg"
image = cv2.imread(filename, 1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image", image)
cv2.imshow("Gray image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Images/3-1.bmp", image)
cv2.imwrite("Images/3-2.bmp", gray)
