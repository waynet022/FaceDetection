import numpy as np
import cv2 as cv
from name_reader import read_names
import argparse


def parser():
    parser = argparse.ArgumentParser(description='Face Training')
    parser.add_argument('--image', type=str, required=True, help='Path to image')
    parser.add_argument('--names', type=str, required=True, help='Path to names file')
    parser.add_argument('--yml', type=str, required=True, help='Path to yml file')

    return parser.parse_args()

def run():
    args = parser()
    names_file = args.names
    people = read_names(names_file)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    # features=np.load('features.npy', allow_pickle=True)
    # labels=np.load('labels.npy')

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read(args.yml)

    img = cv.imread(args.image)
    cv.imshow('Person', img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')
        cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Image', img)
    cv.waitKey(0)

if __name__=='__main__':
    run()