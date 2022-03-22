import cv2 as cv
img = cv.imread('images/salman.jfif') #reading image
cv.imshow('1',img) # a new window will open to show read image, a resized  image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)# used for bluring the image
#cv.imshow('BLur',blur)
canny = cv.Canny(img, 125, 175)# is used to find the edges of image
cv.imshow('canny',canny)
dilated = cv.dilate(canny, (7,7),iterations = 3) # can assume that dilate can bold the edges 
cv.imshow('dilated',dilated)
cv.waitKey(0)
# another to resize the image
resized = cv.resize(img,(200,500))
cv.imshow('resized',resized)
cv.waitKey(0)
