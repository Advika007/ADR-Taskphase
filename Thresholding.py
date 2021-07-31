import cv2
import cv2 as cv
import numpy as np

img=cv2.imread('fruits.jpg')
#The path to input images are specified on which thresholding is to be applied.

#Thresholding- This is segmentation technique used used for separating an object from its background.
#The process of thresholding involves comparing each pixel of an image with a predefined threshold value. This type of comparison of each pixel of an image to a threshold value divides all the pixel of input image into two groups.
#The first group involves pixels having intensity value lower than the threshold value.
#The second group involves pixels having the value greater than the threshold value.

ret, th1= cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#Inside the bracket parameters are input image array(which must be grayscale), thresholdvalue-Value of threshold below and above which pixel values will change accordingly, maximum value that can be assigned to a pixel, the type of thresholding applied

#In binary thresholding we are comparing each and every pixel of original image to 127 and if the value of the pixel is less than 127, the value is assigned to zero and if the value of pixel is greater than 127 the pixel value is assigned to 255
#This is binary threshold which means it is either 0 or 1.

ret,th2=cv2.threshold(img,127,255,cv.THRESH_BINARY_INV)
#This threshold technique gives the inverse result of what we get from thresh binary. If pixel value is less than 127, pixel value 255 is assigned, and if the pixel is greater 127 the pixel value is assigned 0.

ret, th3= cv2.threshold(img ,127,255, cv.THRESH_TRUNC)
#In this threshold technique the value pixel will not change upto threshold value that is 127,and after the threshold value the pixel the assigned pixel value remains same that is 127 which is the threshold value.

ret, th4=cv2.threshold(img,127,255,cv.THRESH_TOZERO)
#In this technique the value less than threshold value that is 127 will be assigned zero and pixel value greater than 127 will not change.

ret, th5=cv2.threshold(img,127,255,cv.THRESH_TOZERO_INV)
#This is inverse of thresh_tozero , here the pixel value greater than threshold value is assigned zero and pixel value less than threshold value remains same,

#Adaptive thresholding- This is a method where the threshold value is calculated for a smaller region. Therefore there will be different threshold value for different regions.
#When the lighting is different in different region of the image, we use this method.

ret, th6= cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,11,2)
#Parameters inside the bracket is input image array, maximum value that can be assigned to a pixel, adaptive method decides how the threshold value is calculate, block size-this decides the size of the neighborhood area,Value of C
#ADAPTIVE_THRESH_MEAN_C Method-In this method threshold value iss the mean of the neighborhood area. Threshold value= Mean of the neighbourhood area value- constant

ret, th7= cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,11,2)
#THRESHOLD VALUE= Gaussian weighted sumof the neighbourhood values- constant value

cv.imshow('img',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.imshow('th5',th5)
cv.imshow('th6',th6)
cv.imshow('th7',th7)

cv.waitKey(0)
cv.destroyAllWindows()