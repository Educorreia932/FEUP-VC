import cv2

filename = "zappa_lain.jpg"
img = cv2.imread(filename, 1)

print(f"Width: {img.shape[0]}")
print(f"Height: {img.shape[1]}")

cv2.imshow(filename, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
