import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    edges = cv2.Canny(frame, 140, 140)


    cv2.imshow('edges', edges)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('frame', frame)
    cv2.imshow('soblex', sobelx)
    cv2.imshow('sobely', sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()