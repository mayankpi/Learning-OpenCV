import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#								=> 0
#CAN ALSO USE -- IMREAD_COLOR => 1
#IMREAD_UNCHANGED => -1



"""cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 130], 'c', linewidth = 3)
plt.show()