#Background subtraction is a way of eliminating the background from image.
import numpy as np
import cv2

#create objects to signify the algorithm we are using for background subtraction
 #Gaussian mixture based algorithm
fgbg2=cv2.createBackgroundSubtractorMOG2()


#capture frames from a webcam
cap= cv2.VideoCapture(0)
while(1):
    ret, img= cap.read()

    fgmask2 = fgbg2.apply(img)

#apply mask for background subtraction

    cv2.imshow('img',img)
    cv2.imshow('mog2', fgmask2)


    k= cv2.waitKey(30) & 0xFF
    if k == 27:
        break;
    cap.release()
    cv2.destroyAllWindows()




