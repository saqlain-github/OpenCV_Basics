import numpy as np
import cv2

image = np.zeros((200,200))
cv2.rectangle(image, pt1=(20,10),pt2=(100,150),color=(205), thickness=-1)


cv2.imshow("mask", image)
cv2.waitKey(0)
cv2.destroyAllWindows()