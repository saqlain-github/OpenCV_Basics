import cv2
import numpy as np

import cv2

image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\6png.png",flags=0)

'''
Four Types of operations

1. Erosion (A 0- B) -> decrease the noise (features get highlighted) -> 
2. Dilation (A 0+ B) -> increasing noise()
3. Opening -> followed by erosion
4. Closing -> followed by dilation
'''

kernal = np.ones((3,3),dtype=np.uint8)

image_erosion = cv2.erode(image,kernal,iterations=2)
image_dilation = cv2.dilate(image,kernal,iterations=2)

opening = cv2.morphologyEx(src=image,op=cv2.MORPH_OPEN,kernel = kernal, iterations=5)
closing = cv2.morphologyEx(src=image,op=cv2.MORPH_CLOSE,kernel = kernal, iterations=5)

gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel=kernal)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel=kernal)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel=kernal)

cv2.imshow("closing",blackhat)
#cv2.imshow("opening",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()