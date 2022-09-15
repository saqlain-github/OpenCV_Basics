import  cv2
import numpy as np

image = cv2.imread(filename=r"../images/prime.png", flags = 1)

# Thresh_Binary       => pixel >= thresold = 255 : 0
# Thresh_Binary_INV   => pixel >= thresold = 0 : 255
# Thresh_TRUNC        => Pixel >= threshold = Threshold
# thresh_tozero       => Pixel <= Threshold = 0 :  pixel
# thresh_tozero_inv   => Pixel >= Threshold = 0:  pixel
ret,thresh = cv2.threshold(src=image, thresh=100, maxval=255, type=cv2.THRESH_TRUNC)


cv2.imshow('image',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()