import cv2
import numpy as np
import random

filename = "zappa_lain.jpg"
image = cv2.imread(filename, 1)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
v, s, h = cv2.split(hsv)

cv2.imshow("Hue channel", h)
cv2.imshow("Saturation channel", s)
cv2.imshow("Value channel", v)

s += 100

merged = cv2.merge((v, s, h))

cv2.imshow("Merged", cv2.cvtColor(merged, cv2.COLOR_HSV2BGR))

cv2.waitKey(0)
cv2.destroyAllWindows()
