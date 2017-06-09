import cv2
import numpy as np


#hsv => hue saturation value
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([50, 50, 190])
    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32)/225
    smoothed = cv2.filter2D(result, -1, kernel)

    gaussian = cv2.GaussianBlur(result, (15, 15), 0)

    median = cv2.medianBlur(result, 15)

    bilateral = cv2.bilateralFilter(result, 15, 75, 75)

    cv2.imshow('gausssian', gaussian)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)
    cv2.imshow('smoothed', smoothed)
    # cv2.imshow('frame', frame)
    #cv2.imshow('hsv', hsv)
    #cv2.imshow('mask', mask)
    #cv2.imshow('result', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
