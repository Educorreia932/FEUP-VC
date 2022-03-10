import cv2

filename = "Images/lizard.jpg"
img = cv2.imread(filename, 1)

cv2.imwrite("Images/2.bmp", img);