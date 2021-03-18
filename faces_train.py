import cv2 as cv2
import os
import numpy as np

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

if __name__=='__main__':
    name_file = 'people.names'
    face_location = 'images/faces/train'

    people = read_names(name_file)
    face_folders=face_images(face_location)