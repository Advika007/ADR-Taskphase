#bitwise operation on binary image
#organizing imports
import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
#image is created, rows ,columns,channels and data type is specified inside the bracket.
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
#rectangle is drawn inside the image , the 4 coordinates of the rectangle is specified and the rectangle is filled with white colour.
img2= cv2.imread("black.png")
# path to input images are specified and images are loaded with imread command

#size of the images should be same, so we have to resize the image
img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))

bitAnd= cv2.bitwise_and(img2,img1)
#This will work on logic and concept,black region of the image will be 0 and white region will be 1, so while performing bitwise add operation the part of images where both image is white, is set white in final image.

bitOr= cv2.bitwise_or(img2,img1)
#This will work on logic or concept.

bitNot=cv2.bitwise_not(img1)
#this methods gives the output opposite of source, if the image input is 1 the output will be 0.

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bitAnd",bitAnd)
cv2.imshow("bitOr",bitOr)
cv2.imshow("bitNot",bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()