import cv2
import mediapipe as mp
import time
import math

class HandDetector():
    def __init__(self, mode=False, maxHands=2, complexity=1, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity, self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLMs in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLMs, self.mpHands.HAND_CONNECTIONS)
        
        return img

    
    def findPosition(self, img, handId=0, draw=True):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            targetHand = self.results.multi_hand_landmarks[handId]
            for id, lm in enumerate(targetHand.landmark):
                h, w, c = img.shape
                cx , cy = int(lm.x * w), int(lm.y * h)

                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (230, 185, 4), cv2.FILLED)
        return self.lmList

    def fingersUp(self):
        fingers = []

        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        return fingers

    def findDistance(self, p1, p2, img, draw=True, r=5, t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1+x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1),  (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1),  r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img


# dummy
def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector() #

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        landmarkList = detector.findPosition(img, draw=False)
        print(landmarkList)

        cv2.imshow('Camera', img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()