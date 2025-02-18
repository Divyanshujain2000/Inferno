#!/usr/bin/env python
from collections import deque
import numpy as np
#import imutils
import cv2

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

def main():
    #WindowName="live"
    #cv2.namedWindow(WindowName)
    cap = cv2.VideoCapture(1)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    while ret:

        ret,frame = cap.read()
        #output = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #frame = imutils.resize(frame, width=600)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if x < 300 :
                print("move left "+ str(-1*(x-300)) +" spaces")
            else : 
                print("move right " + str(-1*(300-x)) +" spaces")
                   
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        
        
        
        
        #cv2.imshow(WindowName,output)
        cv2.imshow("color original",frame)
        cv2.imshow("Mask", mask)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindow()

    cap.release()



if __name__ == "__main__":
    main()
