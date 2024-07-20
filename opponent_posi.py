import cv2
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
cap = cv2.VideoCapture(0)
address="http://192.168.94.147:8080"
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=True)

    if lmList:
    
        right_palm_x, right_palm_y = lmList[17][1], lmList[17][2]

        print(f"Right Palm Coordinates - X: {right_palm_x}, Y: {right_palm_y}")

    if bboxInfo:
        for bbox in bboxInfo:
            if len(bbox) == 4:
                x, y, width, height = bbox  
                print(f"Opponent bat coordinates - X: {x}, Y: {y}")
            else:
                print(f"Invalid bbox format: {bbox}")

    cv2.imshow("Tennis", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()