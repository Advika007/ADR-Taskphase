#Arithmetic operation on images
import numpy as np
import cv2

img= cv2.imread('fruits.jpg')
img2=cv2.imread('Lena.png')
#The path to input images are specified an dimages are loaded with imread command.

print(img.shape)
#This returns tuple of number of rows, columns and channels
print(img.size)
#This returns total number of pixels in the image
print(img.dtype)
#This returns datatype of the image.

#Operation 1- SPLIT AND MERGE
b,g,r= cv2.split(img)
#This splits the source image into 3 single channels.
img= cv2.merge(b,g,r)
#This takes single channel images and combine them to make multi channel image.

copy= img[273:340, 330:390]
#using this we select the part of the image we want to copy.
img[273:333,100:160]=copy
#we select the part of the image on which we want to paste.

#Masking- Masking allows us to focus only on the portion of image that interests us.

#Operation 2- ADDING OF IMAGES
#In order to add two images, the images should be of same size.So we will resize the image.

img= cv2.resize(img, (512,512))
img2=cv2.resize(img2,(512,512))

dst=cv2.add(img, img2)
#This directly adds up image pixel in the two images.

dst1= cv2.addWeighted(img,0.9,img2,0.1,0 )
#In this method we specify the weight of each image to be added.
#Inside the bracket we write, first input image array,weight of the first input image elements to be applied to the final image, second input image array, weight of the second input image element to be applied to the final image, gamma value)

cv2.imshow('image',img)
cv2.imshow('addition',dst1)
#to display the resultant image.
cv2.waitKey(0)
cv2.destroyAllWindows()
