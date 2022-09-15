import cv2
import numpy as np

import cv2

image = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\dogpng.png",flags=0)

image = cv2.copyMakeBorder(src=image, top=100, bottom=50, left = 30, right = 0, borderType=cv2.BORDER_ISOLATED)
cv2.imshow("images",image)
cv2.waitKey(0)
cv2.destroyAllWindows()