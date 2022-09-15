import cv2

image1 = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\dogpng.png",flags=1)
image2 = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\prime.png",flags=1)
# Addition, substraction and Multiplicaiton if pixel > 255 = 0 and pixel < 0 : 0
# Division pixel= floor(pixel)
print(image1.shape,image2.shape)
image2 = cv2.resize(image2, dsize=(image1.shape[1],image1.shape[0]))
print(image1.shape,image2.shape)
#cv2.add(image1,image2)
#final = cv2.divide(image1,image2,scale=1000) # scale -> 1/2 = 0.5 *2 =1 and apply round operator
final = cv2.addWeighted(src1=image1,src2=image2, alpha=0.5, beta = 0.1, gamma = 0) # alpha and gamma weights of each image, gamma constant added to output of pixel
# like adding brightness

cv2.imshow("images",final)
cv2.waitKey(0)
cv2.destroyAllWindows()