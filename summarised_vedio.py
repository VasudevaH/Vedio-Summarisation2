# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:29:08 2018

@author: vasudeva
"""

import cv2
import numpy as np
import imutils
from random import randint

count=0
while count<673:
    frame1=cv2.imread("photoo{}.png".format(count))
    cv2.imshow("summarised",frame1)
    count=count+1
    k=cv2.waitKey(1)
    if k==27:
        cv2.destroyAllWindows()
cv2.destroyAllWindows()