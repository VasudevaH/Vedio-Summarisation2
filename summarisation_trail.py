# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:47:33 2018

@author: vasudeva
"""

import cv2
import numpy as np
import imutils
from random import randint

fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg=cv2.createBackgroundSubtractorMOG2()

cap=cv2.VideoCapture("Home2.mp4")

frame_count=0
summarised_framecount=0
dim=(600,600)
first=0
while True:
    frame_count=frame_count+1
    ret,frame=cap.read()
    if ret==True:
        rframe=cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
        frame1=fgbg.apply(rframe)
        
        if first==0:
            cv2.imwrite("photoo0.png",frame)
            first=first+1
        frame1=cv2.GaussianBlur(frame1,(5,5),0)

        kernel = np.ones((5,5),np.uint8)
        frame1=cv2.erode(frame1,kernel,iterations=1)
        kernel = np.ones((3,3),np.uint8)
        frame1=cv2.dilate(frame1,kernel,iterations=1)
#        

#        ret,frame1 = cv2.threshold(frame1,127,255,cv2.THRESH_TOZERO)
#        frame1=cv2.dilate(frame1,kernel,iterations=4)
        
        
        cnts = cv2.findContours(frame1.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]  
        
        detection_count=0
        for c in cnts:
            if cv2.contourArea(c)<400:
                continue
            else :
                detection_count=detection_count+1
            (x,y,w,h) = cv2.boundingRect(c)
            
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            
            
            cv2.drawContours(frame1,[box],0,(255,0,0),2)
            
            
        if detection_count>0:
            summarised_framecount=summarised_framecount+1
            cv2.imshow("summarised",frame1)
            
            cv2.imwrite("photoo{}.png".format(summarised_framecount),frame)
            k=cv2.waitKey(1)
       #
        
            if(k==27):
                break
        
  
    else:
        break
print("frame_count=",frame_count)
print("summarised_framecount=",summarised_framecount)
cap.release()
cv2.destroyAllWindows()