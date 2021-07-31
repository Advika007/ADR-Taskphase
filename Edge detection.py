import cv2
import numpy as np
from matplotlib import pyplot as plt
# Coverting to gray scale-
img= cv2.imread('fruits.jpg', cv2.IMREAD_GRAYSCALE)
#Convulating with proper kernel-
# The laplacian edge detector uses only one kernel.
lap= cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap= np.uint8(np.absolute(lap))
#Sobel edge method detects edge based on the first order derivative.It calculates the first derivative seperately for x and y axes.
# SobelX- Horizontal edge detection
# SobelY- Vertical edge detection
sobelX= cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY= cv2.Sobel(img,cv2.CV_64F,0,1)
# In canny method we need to values, threshold 1 and threshold 2,  any gradient value larger than threshold2 are considered to be an edge.
#Any value below threshold1 are considered not be edge.
edges= cv2.Canny(img,100,200)
# Any gradient value more than 200 is edge and any value less than 100 is non edge.

#SobelX and SobelY images are float data type. So they are coverted back to 8-bit unsigned integer.
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))
#We can combine our sobel gradient images using  this method-
sobelCombined= cv2.bitwise_or(sobelX,sobelY)
titles= ['image','laplacian','sobelX','sobelY','sobelCombined','Canny']
images= [img,lap,sobelX,sobelY,sobelCombined,edges]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()