import TuxasHandtracking as th
import cv2
import time

cap = cv2.VideoCapture(0)
detector = th.HandDetector(maxHands=4, detectionConfidence=0.8)

while True:
    try:
        success, img = cap.read()
        img = detector.findHands(img)

        lms = detector.findPosition(img, draw=False)

        cv2.imshow('Camera', img)
        cv2.waitKey(1)

    except:
        print('Canceled')
        break