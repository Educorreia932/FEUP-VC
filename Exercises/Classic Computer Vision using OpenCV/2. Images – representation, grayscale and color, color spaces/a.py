import cv2
import numpy as np

image = np.ones((100, 200, 3), np.uint8) * 122

cv2.line(image, (0, 0), (200, 100), (255, 255, 255), 1)
cv2.line(image, (200, 0), (0, 100), (255, 255, 255), 1)

cv2.imshow("Grayscale", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
