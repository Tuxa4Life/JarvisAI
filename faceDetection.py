import cv2

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the image
cap = cv2.VideoCapture(0)


while True:
    try:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        faces = faceCascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        cv2.imshow("Faces found", img)
        cv2.waitKey(1)
    except:
        print('Canceled')
        break
