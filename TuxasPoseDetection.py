import cv2
import mediapipe as mp

# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose

# pose = mpPose.Pose()
# cap = cv2.VideoCapture(0)
# pTime = 0

# while True:
#     success, img = cap.read()
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = pose.process(imgRGB)

#     if results.pose_landmarks:
#         mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
#         for id, lm in enumerate(results.pose_landmarks.landmark):
#             h, w, c = img.shape
#             cx, cy = int(lm.x * w), int(lm.y * h)


#     cv2.imshow("Image", img)
#     cv2.waitKey(1)

class PoseDetection():
    def __init__(self):
        self.mpDraw = mpDraw = mp.solutions.drawing_utils
        self.mpPose = mpPose = mp.solutions.pose
        self.pose = mpPose.Pose()

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)

        if draw:
            if results.pose_landmarks:
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
        
        return img

def main():
    cap = cv2.VideoCapture(0)
    detector = PoseDetection() #

    while True:
        success, img = cap.read()
        img = detector.findPose(img)

        cv2.imshow('Camera', img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()