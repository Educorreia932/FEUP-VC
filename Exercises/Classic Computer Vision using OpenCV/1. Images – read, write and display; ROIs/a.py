import cv2

filename = "Images/lizard.jpg"
image = cv2.imread(filename)

print(f"Width: {image.shape[0]}")
print(f"Height: {image.shape[1]}")

cv2.imshow(filename, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Images/1.jpg", img);
