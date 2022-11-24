import TuxasHandtracking as th
import TuxasVoiceAssistant as tv
import cv2
import time

cap = cv2.VideoCapture(0)
detector = th.HandDetector(detectionConfidence=0.8, maxHands=1)
voiceAss = tv.VoiceAssistant()

cap.set(3, 1500)
cap.set(4, 1000)

while True:
    try:
        success, img = cap.read()
        img = detector.findHands(img)

        cv2.imshow('Camera', img)
        cv2.waitKey(1)

    except:
        print('Canceled')
        break