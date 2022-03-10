import cv2
import numpy as np
import random

filename = "Images/lizard.jpg"
image = cv2.imread(filename, 1)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow("Hue channel", h)
cv2.imshow("Saturation channel", s)
cv2.imshow("Value channel", v)

cv2.imwrite("Images/6-1.bmp", h)
cv2.imwrite("Images/6-2.bmp", s)
cv2.imwrite("Images/6-3.bmp", v)

s += 100

merged = cv2.merge((h, s, v))
image = cv2.cvtColor(merged, cv2.COLOR_HSV2BGR)

cv2.imshow("Merged", image)

cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("Images/6-4.bmp", image)

