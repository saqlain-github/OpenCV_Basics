import cv2

image1 = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\circlepng.png")
image2 = cv2.imread(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\images\rectangle.jpg")

image2 = cv2.resize(image2, dsize=(image1.shape[1],image1.shape[0]))
final = cv2.bitwise_xor(image1,image2)

cv2.imshow("images",final)
cv2.waitKey(0)
cv2.destroyAllWindows()