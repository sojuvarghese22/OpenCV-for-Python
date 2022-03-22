#pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

people = ['salman khan', 'sharukh khan'] #name of folder which is there in this location E:\NEW DATA\Practising folder\opencv\train'

DIR = r'E:\NEW DATA\Practising folder\opencv\train' #location

haar_cascade = cv.CascadeClassifier('haar_face.xml') #this line is reading about 10000 lines of code from the file which is located at here 'haar_face.xml'

features = [] #list store the faces of peoples 
labels = [] #list store the index of people that are thre in features list

def create_train():
    for person in people:
        path = os.path.join(DIR, person) # to concatenate the location with name of people that are store in features list
        label = people.index(person) # index of people 

        for img in os.listdir(path):
            img_path = os.path.join(path,img)# to concatenate the location with name of people that are store in features list
        

            img_array = cv.imread(img_path)#reading the image
            if img_array is None:
                continue 

            
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) #this will give the cordinate of rectangle (face's rectangle) with height and width

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)