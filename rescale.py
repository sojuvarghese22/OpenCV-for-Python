import cv2 as cv #import cv2 and given a name to that i.e is 'cs'

img = cv.imread('images/1.png') #reading image

#function that resize the image(reduce height and weight of image)
def rescaleFrame(frame, scale=0.75): #frame means persecond how much image shown
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)


    dimensions = (width,height) 

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  #resize frame will be returned



resized_image = rescaleFrame(img,0.2)  #function call for resizing image
cv.imshow('screenshot', img) # a new window will open to show read image, a normal image 

cv.imshow('show',resized_image) # a new window will open to show read image, a resized  image

cv.waitKey(0)

"""if want to resize image than comment the code that is there for resizing the video and vice versa"""



capture = cv.VideoCapture('videous/demo1.mp4')

#resizing the video by frame by frame and will continue the till the specified time completes or if 'd' is pressed
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.2)
    cv.imshow('showing',frame)
    cv.imshow('video resized',frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 