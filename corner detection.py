#import the libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

img= cv2.imread('fruits.jpg')
# to read the image

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# this method converts image to gray scale image

# to detect corners of the image we use goodFeatureToTrack method-
corners= cv2.goodFeaturesToTrack(gray, 25,0.05,9)
# parameter 1 - image array
# parameter 2- max number of corners
#parameter 3- min distance between corners
#parameter 4- block size
corners= np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    #we make a circle at each point that we think is a circle
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('Corner',img)



