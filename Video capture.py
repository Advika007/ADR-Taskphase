import cv2
import numpy as np

cap= cv2.VideoCapture(0) #create input file
while True: #check if camera opened successfully
    ret, frame = cap.read() #capture frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame) #display frame
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0x0FF == ord('q'): #returns unicode point of q
       break
    print(cv2.waitKey(1))
cap.release()
cv2.destroyAllWindows()
#cv2.waitkey()- returns 32 bit integer corresponding to the pressed key
