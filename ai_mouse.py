import cv2
import numpy as np
import time
import TuxasHandtracking as th
import pyautogui as pg

wCam, hCam = 640, 480 
wScr, hScr = pg.size()
frameR = 130
smoothing = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = th.HandDetector()
    
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    landmarkList = detector.findPosition(img, draw=False)

    if len(landmarkList) != 0:
        x1, y1 = landmarkList[8][1:]
        x2, y2 = landmarkList[12][1:]

        fingers = detector.fingersUp()

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (200, 200, 0), 2)
        if fingers[1] and not fingers[2]:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothing
            clocY = plocY + (y3 - plocY) / smoothing
            
            pg.moveTo(clocX, clocY) 
            plocX = clocX
            plocY = clocY

        if fingers[1] and fingers[2]:
            length, img = detector.findDistance(8, 12, img)
            
            if length < 30:
                pg.click()

        

    cv2.imshow("Tracking", img)
    cv2.waitKey(1)