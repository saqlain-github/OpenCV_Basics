# image translatin or image shifting

import numpy as np
import cv2

image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\google.png", flags=1)


for i in range(5):
    #image = cv2.pyrDown(image) #divide by 2
    image = cv2.pyrUp(image) # multiplly by 2
    #cv2.imshow("images", )
    cv2.imshow("mask", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
