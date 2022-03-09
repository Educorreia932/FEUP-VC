import cv2
from copy import copy

filename = "zappa_lain.jpg"
img = cv2.imread(filename, 1)

def mouseRGB(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    b = img[y, x, 0]
    g = img[y, x, 1]
    r = img[y, x, 2]
    color = f"{r}, {g}, {b}"

    if event == cv2.EVENT_LBUTTONDOWN:
        img[y, x, 2] = int(input("R (0-255): "))
        img[y, x, 1] = int(input("G (0-255): "))
        img[y, x, 0] = int(input("B (0-255): "))
        
        print()

    img_copy = copy(img)
    cv2.putText(img_copy, color, (x, y), font, 1, (255, 255, 0), 2)
    cv2.imshow(filename, img_copy)

cv2.namedWindow(filename)
cv2.setMouseCallback(filename, mouseRGB)
cv2.imshow(filename, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
