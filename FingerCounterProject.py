import cv2
import os
import time
import HandTrackingModule as htm


FolderPath="FingersPics"
myList=os.listdir(FolderPath)
overlayList=[]

for imPath in myList:
    image=cv2.imread(f'{FolderPath}/{imPath}')
    overlayList.append(image)

wCam,hCam=1540,580
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector=htm.handDetector(detectionCon=0.9,trackCon=0.6)

tipIDs= [4,8,12,16,20]

while True :
    success,img=cap.read()
    img =detector.findHands(img)
    lmList =detector.findPositions(img,draw=False)
    #print(lmList)

    if len(lmList)!=0 :
        fingers =[]
        # thumb
        if lmList[20][1]-lmList[4][1]<0:
            if (lmList[4][1] > lmList[3][1]):
                fingers.append(1)
            else:
                fingers.append(0)
        else :
            if (lmList[4][1] < lmList[3][1]):
                fingers.append(1)
            else:
                fingers.append(0)
       #4 fingers
        for id in range(1,5):
            if lmList[tipIDs[id]][2]<lmList[tipIDs[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers=fingers.count(1)
        #print(totalFingers)
        overlay_image = overlayList[totalFingers]
        new_w = 200
        new_h = 250
        resized_overlay = cv2.resize(overlay_image, (new_w, new_h))
        img[0:new_h, 0:new_w] = resized_overlay

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'fps :{int(fps)}',(540,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)

    cv2.imshow("img",img)
    cv2.waitKey(1)
