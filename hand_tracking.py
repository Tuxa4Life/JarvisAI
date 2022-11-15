import TuxasHandtracking as th
import cv2
import time

cap = cv2.VideoCapture(0)
detector = th.HandDetector()

while True:
    try:
        success, img = cap.read()
        img = detector.findHands(img)

        cv2.imshow('Camera', img)
        cv2.waitKey(1)

    except:
        print('Canceled')
        break