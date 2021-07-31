import numpy as np
import cv2

img = cv2.imread('fruits.jpg',1)
#input image in which line has to be drawn.
cv2.line(img,(0,0),(150,150),(100,100,0),15)
#parameter 1- input image array
#parameter 2- starting coordinate
#parameter 3- ending coordinate
#parameter 4- The color of line to be drawn in BGR format
#parameter 5- Thickness of the line
cv2.circle(img,(100,150),100,(255,0,0),-1)
#to draw a circle on a image we use this method
#parameter 1- input image array
#parameter 2- centre coordinates of circle
#parameter 3- Radius of circle
#parameter 4- color in BGR format
#parameter 5- Thickness of circle border line, if the thickness is -1,it will fill th ecircle with the specific colour.
cv2.imshow('image',img)
#display the resulting image
#parameter 1- window name
cv2.waitKey(0)
cv2.destroyAllWindows()