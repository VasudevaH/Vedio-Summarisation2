# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:47:33 2018

@author: vasudeva
"""

import cv2
import numpy as np
import imutils
from random import randint
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class c1:
    summarised_framecount=0
    def f1(self):
        fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()   #Mixture of Gaussian model which is Robust to lighting chnages,Shadows


        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)
        cap=cv2.VideoCapture(filename) #Input video file name

        frame_count=0 #counter to count number of frames in original video
        summarised_framecount=0 #Counter to count number of frames in summarised video
        dim=(600,600) #Resizing the  frames of the video to the dimension (600,600) 
        first=0 
        while True:
            frame_count=frame_count+1
            ret,frame=cap.read()
            if ret==True:
                rframe=cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
                frame1=fgbg.apply(rframe)
                
                if first==0:
                    cv2.imwrite("out/photoo0.png",frame) #Writing the first frame of the video to the summarised output video
                    first=first+1
                
                frame1=cv2.GaussianBlur(frame1,(5,5),0) #Smootening the noise present in the videoo frame
                kernel = np.ones((5,5),np.uint8)
                frame1=cv2.erode(frame1,kernel,iterations=1) #Marphological operation to decrese the whitenoise in the frame
                kernel = np.ones((3,3),np.uint8)
                frame1=cv2.dilate(frame1,kernel,iterations=1) #Marphological operation to restore the shap of the objects present in the frame

                #Function which finds contours present in the frame
                cnts = cv2.findContours(frame1.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
                cnts = cnts[0] if imutils.is_cv2() else cnts[1]  
                
                detection_count=0 #Counter to count number of objects prsent in the given frame
                for c in cnts:
                    if cv2.contourArea(c)<400: #Sensitivity measure  to ignore small objects.Increaing this value decreases the number of objects identified 
                        continue
                    else :
                        detection_count=detection_count+cv2.contourArea(c)
                    (x,y,w,h) = cv2.boundingRect(c)
                    
                    rect = cv2.minAreaRect(c)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    
                    
                    cv2.drawContours(frame1,[box],0,(255,0,0),2 )#drawing contours on the background subtracted frame,after all the above operations were done
                    
                    
                if detection_count>3000: #Retaining the frame if the number of objects identified is greater than the specified number i'e is  0 in this case
                    summarised_framecount=summarised_framecount+1
                    cv2.imshow("summarised",frame1)
                    
                    #saving the frames to your pwd(present working drectory) with names as fallows(photoo0, photoo1...)
                    cv2.imwrite("out/photoo{}.png".format(summarised_framecount),frame)
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
