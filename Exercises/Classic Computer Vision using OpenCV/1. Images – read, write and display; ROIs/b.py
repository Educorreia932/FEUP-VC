import cv2

filename = "zappa_lain.jpg"
img = cv2.imread(filename, 1)

cv2.imwrite(f"{filename.split('.')[0]}.bmp", img);