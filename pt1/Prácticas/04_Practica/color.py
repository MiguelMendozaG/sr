#Detecta el color rojo
import cv2
import numpy as np
import imutils
 
img = cv2.imread('cuatro.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([178, 179, 0])
upper_range = np.array([255, 255, 255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('image', img)
cv2.imshow('mask', mask)
 
while(True):
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv2.destroyAllWindows()

