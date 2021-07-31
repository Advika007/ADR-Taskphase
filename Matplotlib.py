import cv2
from matplotlib import pyplot as plt
#Pyplot is a collection of functions in the popular visualization package Matplotlib. Its function is to manipulate elements of a figure, such as creating a figure,creating plotting area, adding plotting labels,etc.

img = cv2.imread('Lena.png',-1)
#path of the input image
cv2.imshow('img',img)
#to display the output image using open cv imshow method

plt.imshow(img)
#to display image using matplotlib

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
#opencv reads the image in BGR format
#matplotlib reads image in RBG format

