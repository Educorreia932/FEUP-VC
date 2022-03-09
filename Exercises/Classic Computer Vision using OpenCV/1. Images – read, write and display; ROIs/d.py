import cv2

filename = "zappa_lain.jpg"
image = cv2.imread(filename, 1)
roi = cv2.selectROI(image)

cv2.namedWindow(filename)
cv2.imshow(filename, image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]])
cv2.waitKey(0)
cv2.destroyAllWindows()
