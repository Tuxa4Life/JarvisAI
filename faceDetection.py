import cv2
import TuxasHandtracking as th

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
detector = th.HandDetector()

while True:
    try:
        success, img = cap.read()
        faces = faceCascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        cv2.imshow("Faces found", img)
        cv2.waitKey(1)
    except:
        print('Canceled')
        break
