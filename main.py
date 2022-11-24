import cv2
import mediapipe as mp
import TuxasHandtracking as th
import TuxasFaceDetectionModule as tf

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose

pose = mpPose.Pose()
detector = th.HandDetector()
fDetector = tf.FaceDetector(faceCascade) 
cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img = fDetector.findFace(img)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)


    cv2.imshow("Image", img)
    cv2.waitKey(1)