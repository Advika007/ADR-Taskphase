import cv2
import numpy as np

img= cv2.imread('fruits.jpg')

cv2.imshow('img',img)
cv2.waitKey(0)

#Gaussian blur- This method uses gaussian function. Used to reduce image noise and reduce detils.
Gaussian= cv2.GaussianBlur(img, (7,7),0)
cv2.imshow('Gaussian blurring', Gaussian)

#Median blur
median = cv2.medianBlur(img,5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

#Bilateral blur
Bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Bilateral blurring', Bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()