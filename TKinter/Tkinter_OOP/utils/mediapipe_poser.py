import cv2
import mediapipe as mp
import time

class poseDetector():    
    def __init__(self, mode=False, upperbody=False, smoothness=True,
                 detectConf=0.5, trackConf=0.5):
        self.mode = mode
        self.upperbody = upperbody
        self.smoothness = smoothness
        self.detectConf = detectConf
        self.trackConf = trackConf
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            static_image_mode=self.mode,
            model_complexity=self.upperbody,
            smooth_landmarks=self.smoothness,
            min_detection_confidence=self.detectConf,
            min_tracking_confidence=self.trackConf
        )

    def findPose(self, img, draw=True):
        imgRBG = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2RGB
        )
        self.results = self.pose.process(image=imgRBG)
        
        if self.results.pose_landmarks:
            if draw:
                # print(self.results.pose_landmarks)
                self.mpDraw.draw_landmarks(
                    image=img,
                    landmark_list=self.results.pose_landmarks,
                    connections=self.mpPose.POSE_CONNECTIONS
                )
        return img
    
    def getPosition(self, img, draw=True):        
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(
                        img,
                        center=(cx, cy),
                        radius=5,
                        color=(255, 0, 0),
                        thickness=cv2.FILLED,
                    )
        return lmList
    
def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    
    detector = poseDetector()
    
    def change_res(width, height):
        cap.set(3, width)
        cap.set(4, height)
    
    change_res(360, 240)
    
    while True:
        success, img = cap.read()
        img = detector.findPose(img, draw=True)
        lmList = detector.getPosition(img, draw=False)
        if len(lmList != 0):
            print(lmList[14])  # just draw the body part no.14
            cv2.circle(
                img,
                center=(lmList[14][1], lmList[14][2]),
                radius=15,
                color=(0, 0, 110),
                thickness=cv2.FILLED
            )

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        cv2.putText(
                img=img,
                text=str(int(fps)),
                org=(10, 70),
                fontFace=cv2.FONT_HERSHEY_PLAIN,
                fontScale=3,
                color=(255, 255, 0),
                thickness=3
            )
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    
if __name__ == "__main__":
    main()
    