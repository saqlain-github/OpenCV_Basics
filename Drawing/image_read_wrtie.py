import  cv2
import numpy as np


print(cv2.__version__)

# read image in colour foramt without alpha channel
# colour image = 1 ny default
# cv.imread_colour

# tp read image in grey scale flag = 0 or cv2.image_greyscale

# to read image as it is with alpha channel flag = -1 or cv2.image_unchanged
#aplha -  transperancy in images, mostly in .png


image = cv2.imread(filename=r"../images/prime.png", flags = 1)
width = 300
height = 500
dim = (width,height)
print(image.shape)
#cv2.line(image,pt1=(0,0),pt2=(100,100),color=(0,255,0),thickness=5)
#cv2.arrowedLine(image,pt1=(0,0),pt2=(100,100),color=(0,255,0),thickness=5)



cv2.imshow("YOLO",image)

'''
print(image[0:100,0:10])
image[np.where(image == 255)] = 0
cv2.imshow("Nothing",image)


image2  = cv2.resize(image, dsize=(0,0),fx = 0.1, fy = 0.1)
print(image2.shape)
cv2.imshow('OutputImage',image2)
cv2.imwrite("dropped/resized.png",image2)
'''



cv2.waitKey(0)
cv2.destroyAllWindows()