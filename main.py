from hand_tracking_module import handDetector
from hue_api import hueAPI
import cv2
import time
import math





def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    hue = hueAPI()
    while True:
        # save the frame of the video cap to img 
        success, img = cap.read()

        img = detector.findHands(img)
        lmList = detector.findPos(img)
        if len(lmList) != 0:
            # get x, y positions of thumb 
            thumb = lmList[4]
            # get x, y positions of finger 
            index = lmList[8]
            # get distance of the two
            distance = get_distance(thumb, index)
            print(distance)
            # conver the distance to a percentage
            percent = convert_to_percent(distance)
            # change brightness to percent given by distnace 
            hue.brightness(percent)

            # present current brightness percent on screen 
            cv2.putText(img, str(percent), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()



def get_distance(thumb, index):
    # param: x,y cords of thumb and index 
    # use distance formula to calculate the distance between thumb and finger 
    # return distance 
    x, y = thumb[1], thumb[2]
    x2, y2 = index[1], index[2]

    distance = math.sqrt(math.pow(x2-x,2) + math.pow(y2-y,2))

    return distance




def convert_to_percent(distance):
    # param distance of the thumb and index 
    # turn the distance into a percentage 0-100 so it can be used to change the brightness 
    # return percentage 

    if distance > 100:
        return 100
    percent = int(distance)
    return percent



if __name__ == "__main__":
    main()