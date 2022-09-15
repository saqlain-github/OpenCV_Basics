# Importing OpenCV package
import cv2
import os

# Reading the image
img = cv2.imread(r'E:\iNeuron\5.CV\Practise\OpenCV_Project\images\cricket.png')
img = cv2.resize(img,(900,900))
# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier(r'E:\iNeuron\5.CV\Practise\OpenCV_Project\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\opencv-master\data\haarcascades\haarcascade_eye.xml")

# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 5)
print(faces_rect)
# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
    #print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, text = 'Face', org=(x,y), fontFace= cv2.FONT_HERSHEY_PLAIN, fontScale= 2, color=(0,255,0), thickness=2)

    roi_grey = gray_img[y:y+h, x:x+h]
    roi_color = img[y:y+h, x:x+h]

    eyes = eye_cascade.detectMultiScale(image=roi_grey, scaleFactor=1.5, minNeighbors=1)
    for (ex,ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex +ew, ey + eh), (0, 255, 0), 2)


cv2.imshow('Detected faces', img)

cv2.waitKey(0)