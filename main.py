import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)
capture.set(10, 100)

while True:
    success, img = capture.read()
    img = cv2.flip(img, 1)

    img = cv2.putText(img, 'Pidarast', (100, 100), cv2.QT_FONT_NORMAL, 3, (0, 0, 255))

    cv2.imshow('Window', img)
    cv2.waitKey(1)