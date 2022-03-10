import cv2
import numpy as np
import random

filename = "Images/lizard.jpg"
image = cv2.imread(filename, 1)

b, g, r = cv2.split(image)

cv2.imshow("Red channel", r)
cv2.imshow("Green channel", g)
cv2.imshow("Blue channel", b)

b += 100

image = cv2.merge((b, g, r))

cv2.imshow("Merged", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Images/5-1.bmp", r)
cv2.imwrite("Images/5-2.bmp", g)
cv2.imwrite("Images/5-3.bmp", b)
cv2.imwrite("Images/5-4.bmp", image)
