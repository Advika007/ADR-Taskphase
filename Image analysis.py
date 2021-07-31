import cv2

#To read image from disk
img= cv2.imread('fruits.jpg',cv2.IMREAD_COLOR)
#cv2.imread function reads the image
#first parameter is path of the image
#second parameter is type of flags
#There are 3 flags- 1) IMREAD_COLOR- it specifies to load a color image. We can pass integer value 1 for this flag
# 2) IMREAD_GRAYSCALE- it specifies to load an image in grayscale mode. We can pass integer value 0 for this flag
# 3) IMREAD_UNCHANGED- It specifies to load an image as such. We can use integer value -1 for this.

cv2.imshow('Display',img)
#To create window to display image on screen
#first parameter is window title
#second parameter is input image array

cv2.waitKey(0)
#To hold the windwo on screen, we use this method,first parameter is for holding screen for specified millisecond. It should be positive integer. If 0 is passed as parameter then it will hold the screen until user closes it.

cv2.destroyAllWindows()
#It is for removing window from screen and memory