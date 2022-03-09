import cv2
import numpy as np
import random

def salt_and_pepper(image, prob):
    output = np.zeros(image.shape, np.uint8)
    threshold = 1 - prob 

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()

            if rdn < prob:
                output[i][j] = 0
            
            elif rdn > threshold:
                output[i][j] = 255
            
            else:
                output[i][j] = image[i][j]

    return output

filename = "zappa_lain.jpg"
image = cv2.imread(filename, 1)
image_with_noise= salt_and_pepper(image, 0.05)

cv2.imshow("Image with noise", image_with_noise)

cv2.waitKey(0)
cv2.destroyAllWindows()
