import cv2
import numpy as np

'''
 Just extracting specific colour from the images
 eg:  extracting only blue color objects or parts
 
 BGR is not so helpful, HSV is very useful
'''

image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\google.png",flags=1)

color_bgr = np.uint8([[[255,0,0]]]) #BGR
color_hsv = cv2.cvtColor(src=color_bgr, code = cv2.COLOR_BGR2HSV)
print(color_hsv)
hsv = cv2.cvtColor(image,code= cv2.COLOR_BGR2HSV)

#blue [[[120 255 255]]] HSV

lower_blue = (100,45,105)
higher_blue = (140,50,105)

mask = cv2.inRange(src = hsv, lowerb=lower_blue, upperb=higher_blue)


cv2.imshow("images",hsv)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()