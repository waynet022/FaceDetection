import cv2 as cv
import os
import numpy as np

DIR = 'images/faces/train'
hc_file = 'haar_face.xml'
haar_cascade = cv.CascadeClassifier(hc_file)

def read_names(file):
    name_list = []
    with open(file) as names:
        list = names.read().splitlines()
        for name in list:
            name_list.append(name)
    return name_list

def face_images(train_path):
    folders=[]
    for folder in os.listdir(train_path):
        folders.append(folder)
    return folders

def create_train(people):
    features = []
    labels = []
        
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array=cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
    return features, labels

if __name__=='__main__':
    name_file = 'people.names'
    people = read_names(name_file)
    
    features, labels = create_train(people)
    print('Training done')
    features=np.array(features, dtype='object')
    labels=np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    face_recognizer.train(features, labels)

    face_recognizer.save('face_trained.yml')

    np.save('features.npy', features)
    np.save('labels.npy', labels)