# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:29:08 2018

@author: vasudeva
"""
"""
This pytjhon is used to view the summarised video.

"""
import cv2
import numpy as np
import imutils
from random import randint

count=0
while count<673:  #These the number of frames that are left after summarisation of the video.Note:Change this to the summarised_count which is available after running summarisation_trail.py
    frame1=cv2.imread("photoo{}.png".format(count))
    cv2.imshow("summarised",frame1)
    count=count+1
    k=cv2.waitKey(1)
    if k==27:
        cv2.destroyAllWindows()
cv2.destroyAllWindows()
