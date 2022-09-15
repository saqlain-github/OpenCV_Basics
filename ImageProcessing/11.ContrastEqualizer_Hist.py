import numpy as np
import cv2
import matplotlib.pyplot as plt

#contrast something that helps to distinguish objects in image

image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\cllifs.jpg",flags=0)
#image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\dogpng.png", flags=1)
image = cv2.resize(image,dsize=(720,600))
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Equalize the histogeam of 3rd channel

hsv_image[:,:,0] = cv2.equalizeHist(hsv_image[:,:,0])
equalized_img = cv2.cvtColor(hsv_image,cv2.COLOR_HSV2BGR)

#equ = cv2.equalizeHist(image)

cv2.imshow("mask", image)
#cv2.imshow("equilizer", equ)
cv2.imshow("equilizer", equalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()