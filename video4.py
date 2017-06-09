import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[55, 55] = (255, 255, 255)
px = img[55, 55]

print(px)

watch_face = img[300:400, 250:600]
img[0:100, 0:350] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()