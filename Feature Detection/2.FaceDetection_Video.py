# Importing OpenCV package
import cv2


#inbuilt 0, external 1
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'E:\iNeuron\5.CV\Practise\OpenCV_Project\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=4)
    print(faces)

    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, text='Face', org=(x, y), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 255, 0),
                    thickness=2)


    cv2.imshow('Detected faces', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cap.release()
        break

cv2.destroyAllWindows()