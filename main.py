import cv2
import mediapipe as mp
import TuxasModule as tm

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose

pose = mpPose.Pose()
hDetector = tm.HandDetector()
fDetector = tm.FaceDetector(faceCascade) 
pDetector = tm.PoseDetection()
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = hDetector.findHands(img)
    img = fDetector.findFace(img)
    img = pDetector.findPose(img)


    cv2.imshow("Image", img)
    cv2.waitKey(1)