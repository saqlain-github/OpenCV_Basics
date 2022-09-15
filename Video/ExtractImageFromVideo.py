import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'E:\iNeuron\5.CV\Practise\OpenCV_Project\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r"E:\iNeuron\5.CV\Practise\OpenCV_Project\opencv-master\data\haarcascades\haarcascade_eye.xml")


count = 0

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=3)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, text='Face', org=(x, y), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 255, 0),
                    thickness=2)
        roi_color = frame[y:y + h, x:x + h]
        cv2.imwrite(r'E:\iNeuron\5.CV\Practise\OpenCV_Project\Video\dataset2\image%d041.jpg' % count, roi_color)
        count += 1

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cap.release()
        break

cv2.destroyAllWindows()