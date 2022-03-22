import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8') #creating new image
# n.zeros takes 2 parameter 1. shape(height,width)with color channel

blank[200:300, 300:400] = 0,255,0 #coloring in specific area 
#In rectangle 1st parameter is image on which we have to make rectangle, 2nd origin((0,0)=(x,y),3rd destination drawing((x,y)))
cv.rectangle(blank,(0,0),(100,450),(0,255,0), thickness=3)
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness=3)


cv.circle(blank,(250,250),100,(0,0,255), thickness=3)
cv.putText(blank, 'Hello',(100,225), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("Blank",blank) #used to display the image in new window'''

cv.waitKey(0) #hold the window till any key is not pressed


cv.destroy()