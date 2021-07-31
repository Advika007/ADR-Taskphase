import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread('fruits.jpg',cv2.IMREAD_GRAYSCALE)
#The path of the image to be read is defined , the image will be read in grayscale

ret,mask= cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
#thresholding using thresh binary inverse method

kernal= np.ones((2,2),np.uint8)
#Kernal tells us how to change the value of any given pixel by combining it with different amounts of the neighboring pixels.
#in the parameters we define the size and data type of the kernal

dilation=cv2.dilate(mask,kernal,iterations=2)
#Dilation adds pixels to the boundaries of objects
erosion=cv2.erode(mask,kernal,iterations=2)
#Erosion removes pixels on the object boundaries.
opening= cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
#An erosion followed by a dilation
closing= cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernal)
#A dilation followed by an erosion
mg= cv2.morphologyEx(mask,cv2.MORPH_GRADIENT, kernal)
# It is difference between dilation and erosion of an image
th= cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)
#It is difference between input image and opening

titles=['image','mask','dilation','erosion','opening','closing','mg','th']
images= [img, mask, dilation, erosion, opening, closing,mg,th]
for i in range(8):
     plt.subplots(2,4,i+1), plt.imshow(images[i],'gray')
     plt.title(titles[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
