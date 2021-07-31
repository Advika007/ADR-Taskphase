#Template matching- This is a tecgnique for finding areas of an image that are similar to a patch.
import cv2
import numpy as np

img= cv2.imread('pokemon_1.jpg')

#covert image to grayscale-
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Reading the template using imread method
template= cv2.imread('pokemon_2.jpg',0)

w,h= template.shape[::-1]
#Specify width and height of template

res= cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
#Matching operation

threshold= 0.8

loc= np.where(res >= threshold)
#Store the coordindates of matched area in a array using numpy

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt, (pt[0]+ w,pt[1]+h),(0,255,255),2)

cv2.imshow('Detected',img)