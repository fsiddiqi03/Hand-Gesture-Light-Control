import cv2 
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode=False,maxHands =2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.max_hands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon


        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, 
                                max_num_hands=self.max_hands, 
                                min_detection_confidence=self.detectionCon, 
                                min_tracking_confidence=self.trackCon)

        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw = True):

        # hand tracking needs image to be in RGB convert it from BGR 
        imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # get the landmarks on to the hand using the mpHands.Hands() function
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            # loops through all the hand marks as handLms
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                # draws the handmarks and connect the line using the position of the hand coming results.multi_hand_landmarks 
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


    def findPos(self, img, handNo=0, draw=False):
        # list where the pos of each hand landmark will go 
        lmList= [ ]

        # check for land marks 
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                # get the cords of each landmark 
                cx, cy = int(lm.x*w), int(lm.y*h)
                # add landmark to the list 
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        # save the frame of the video cap to img 
        success, img = cap.read()

        img = detector.findHands(img)
        lmList = detector.findPos(img)
        if len(lmList) != 0:
            print(lmList[4])






        # get fps
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        # present the fps 
        # param: img, fps, size, font, size, color, weight 
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)


        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()









if __name__ == "__main__":
    main()