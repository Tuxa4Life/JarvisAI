import cv2

class FaceDetector():
    def __init__(self, cascade):
        self.cascade = cascade
    
    def findFace(self, img, draw=True):
        faces = self.cascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1, 4)

        if draw:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return img


def main():
    cap = cv2.VideoCapture(0)

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    detector = FaceDetector(faceCascade) 

    while True:
        success, img = cap.read()
        img = detector.findFace(img)

        cv2.imshow('Camera', img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()