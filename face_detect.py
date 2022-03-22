import cv2 as cv
import numpy as np
import os
blank = np.zeros((500,500,3), dtype = 'uint8') #creating new image

blank[:] = 0,255,0
cv.imshow('h',blank)

'''
img = cv.imread('images/salman.jfif') #reading image
cv.imshow('Gray person',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml') #object of CascadeClassifier() with parameter as uri of haar_face.xml
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print("Total faces:", len(faces_rect))
for (x,y,w,h) in faces_rect:
    print(x,y,w,h)131 27 64 64'''

cv.rectangle(blank,(131,27),(0,0,255), thickness=3)
cv.imshow('h',blank)

cv.waitKey(0)



