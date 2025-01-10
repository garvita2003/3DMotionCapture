# Import the libraries
import cv2
from cvzone.PoseModule import PoseDetector # get 33 different landmarks

# Opening the video
cap = cv2.VideoCapture('Video.mp4')

detector = PoseDetector()
posList = []
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    # To find the landmarks and get the bounding box around the object
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = '' # Having all the 33 points in it
        for lm in lmList: # lm in the form of [x, y, z]
            lmString += f'{lm[0]},{img.shape[0] - lm[1]},{lm[2]},' # Reverse in case of unity so img.shape[0]-lm[1]
        posList.append(lmString)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'): # Pressing S button save the file
        with open("AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])