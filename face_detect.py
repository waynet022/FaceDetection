import cv2 as cv
import argparse

def parser():
    parser = argparse.ArgumentParser(description='Face Detection')
    parser.add_argument("--image", type=str, required=True, help='Path to the image')
    parser.add_argument("--neighbors", type=int, help='minNeighbors factor')

    return parser.parse_args()

def convert_gray(image, show=False):
    output = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if show:
        cv.imshow('Gray Image', output)
        cv.waitKey(0)
    return output

def detect_face(image, gray_image, neighbors=3, show=True):
    hc_file = 'haar_face.xml'
    haar_cascade = cv.CascadeClassifier(hc_file)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=neighbors)
    if show:
        print('Number of faces detected: ', len(faces_rect))
        for (x,y,w,h) in faces_rect:
            cv.rectangle(image, (x,y), (x+w, y+h), (0,255,0), thickness=1)
        cv.imshow('Detected Faces', image)
        cv.waitKey(0)

if __name__=='__main__':
    args = parser()
    image_file = args.image
    img = cv.imread(image_file)
    gray = convert_gray(img)
    detect_face(img, gray, args.neighbors)