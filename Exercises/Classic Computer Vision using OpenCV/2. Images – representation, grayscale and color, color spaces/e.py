import cv2
import numpy as np
import random

filename = "zappa_lain.jpg"
image = cv2.imread(filename, 1)

b, g, r = cv2.split(image)

cv2.imshow("Red channel", r)
cv2.imshow("Green channel", g)
cv2.imshow("Blue channel", b)

r += 100

cv2.imshow("Merged", cv2.merge((b, g, r)))

cv2.waitKey(0)
cv2.destroyAllWindows()
