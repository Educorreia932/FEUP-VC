import cv2

filename = "Images/lizard.jpg"
image = cv2.imread(filename, 1)
roi = cv2.selectROI(image)
selected = image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]

cv2.namedWindow(filename)
cv2.imshow(filename, selected)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Images/4.jpg", selected);
