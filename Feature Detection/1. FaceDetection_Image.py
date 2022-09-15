# Importing OpenCV package
import cv2
import os

# Reading the image
img = cv2.imread(r'E:\iNeuron\5.CV\Practise\OpenCV_Project\images\cricket.png')
img = cv2.resize(img,(700,700))
# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier(r'E:\iNeuron\5.CV\Practise\OpenCV_Project\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')

# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 5)
print(faces_rect)
# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
    #print(x, y, w, h)
    cv2.rectangle(gray_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(gray_img, text = 'Face', org=(x,y), fontFace= cv2.FONT_HERSHEY_PLAIN, fontScale= 2, color=(0,255,0), thickness=2)

cv2.imshow('Detected faces', gray_img)

cv2.waitKey(0)