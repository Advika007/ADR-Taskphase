import numpy as np
import cv2
from matplotlib import pyplot as plt

#path to input image specified and image is loaded
image= cv2.imread('fruits.jpg')

mask= np.zeros(image.shape[:2],np.uint8)
#create mask similar to input image with shape and return type

backgroundModel1 = np.zeros((1,65),np.float64)
foregroundModel1 = np.zeros((1,65),np.float64)
# specify the background and foreground model using numpy
# array had 1 row and 65 columns
# all elements are zero
# Data type of array is np.float64

rectangle = (20,100,150,150)
# ROI is defined as the coordinates of rectangle
# Parameter1- Starting point X coordinate
# Parameter2- Starting point y coordinate
# Parameter3- Width
# Parameter4- Height

cv2.grabCut(image,mask, rectangle, backgroundModel1,foregroundModel1,3,cv2.GC_INIT_WITH_RECT)
#Grabcut algorithm is used, number of iterations =3,cv2.GC_INIT_WITH_RECT is used beacuse rectangle mode is used.

mask2 = np.where((mask== 2)|(mask == 0),0,1).astype('uint8')
#The pixels are denoted by 4 flags to denote background andforeground
# 0 and 2 pixels are put to background(0)
# 1 and 3 pixels are put to foreground(1)

image= image* mask2[:,:,np.newaxis]
#The mask is multiplied with input image to get segmented image

plt.imshow(image)
plt.colorbar()
plt.show()
#output image with colorbar