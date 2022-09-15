import cv2

image = cv2.imread(filename=r"../images/prime.png", flags = 1)

#cv2.line(image,pt1=(0,0),pt2=(100,100),color=(0,255,0),thickness=5)
#cv2.arrowedLine(image,pt1=(0,0),pt2=(100,100),color=(0,255,0),thickness=5)

#cv2.circle(image,(100,100),50,thickness=5,color=(255,0,0), lineType=cv2.LINE_4)

#cv2.ellipse(image,center=(100,100),axes=(100,40),angle=0, startAngle=90, endAngle=180, thickness= 5,color=(255,60,0))

#cv2.rectangle(image,pt1=(50,50),pt2=(100,100),color=(100,100), thickness=1)

'''
#triangle
cv2.line(image,pt1=(25,25),pt2=(75,10),color=(0,255,0),thickness=5)
cv2.line(image,pt1=(75,10),pt2=(150,100),color=(0,255,0),thickness=5)
cv2.line(image,pt1=(150,100),pt2=(25,25),color=(0,255,0),thickness=5)

center_point = (((25+75+150)//3),((25+10+100)//3))
cv2.circle(image,center_point,1,thickness=5,color=(255,0,0), lineType=cv2.LINE_4)
print(center_point)
'''


#text
cv2.putText(image,text="Data  Sceitist Saqqi", org=(0,25), fontFace=cv2.FONT_ITALIC,fontScale=0.5, color=(255,0,0), lineType=cv2.LINE_AA)



cv2.imshow("YOLO",image)
cv2.waitKey(0)
cv2.destroyAllWindows()