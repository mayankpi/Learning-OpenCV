import cv2
import numpy
import matplotlib.pyplot as plt

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

img3 = cv2.imread('mainlogo.png')

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]
cv2.imshow('roi', roi)

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('initial mask', mask)

mask_inv = cv2.bitwise_not(mask)


img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('img1_bg', img1_bg)

img3_fg = cv2.bitwise_and(img3, img3, mask = mask)
cv2.imshow('img3fb', img3_fg)

dst = cv2.add( img3_fg, img1_bg)
cv2.imshow('dst', dst)

img1[0:rows, 0:cols] = dst

cv2.imshow('finished image', img1)

cv2.imshow('final mask',mask_inv)


# add = img1 + img2
# add2 = cv2.add(img1, img2)
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
#
# cv2.imshow('weighted', weighted)
# cv2.imshow('cv2 add', add2)
# cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()