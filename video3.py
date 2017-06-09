import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,250), (250,0,0), 5)
cv2.rectangle(img, (30,30), (400,400), (255,255,0), 5)
cv2.circle(img, (100,100), 55, (255,0,255), 7)
pts = np.array([[10,6], [100,100], [180,150], [200,100], [50,70]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,0,0), 1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hey there', (400,400), font, 2, (25,55,155), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()