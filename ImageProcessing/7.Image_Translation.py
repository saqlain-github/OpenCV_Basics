# image translatin or image shifting

import numpy as np
import cv2

image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\google.png", flags=1)

print(image.shape)

s = image.shape
M = np.float32([[1,0,50],[0,1,50]])

shifting = cv2.warpAffine(src=image,dsize=(s[1],s[0]),M = M)

cv2.imshow("images", shifting)
cv2.imshow("mask", image)
cv2.waitKey(0)
cv2.destroyAllWindows()