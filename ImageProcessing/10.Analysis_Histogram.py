import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\dogpng.png", flags=0)
cv2.rectangle(image, pt1=(0,100),pt2=(200,100),color=(205), thickness=-1)

#plt.hist(image.ravel(),256,[0,256])
#plt.show()

b,g,r = cv2.split(image)
hist = cv2.calcHist(image,channels=[0], mask=None, histSize=[256], ranges=[0,256])
hist = cv2.calcHist(image,channels=[1], mask=None, histSize=[256], ranges=[0,256])
hist = cv2.calcHist(image,channels=[2], mask=None, histSize=[256], ranges=[0,256])

cv2.imshow("mask", image)
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()