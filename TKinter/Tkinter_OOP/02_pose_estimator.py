# In[] Libs
import tkinter as tk
from tkinter import ttk
import mediapipe as mp
import cv2, time
from PIL import ImageTk, Image

# In[] Layout
class App(tk.Tk):
    def __init__(self, wm_title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"App Class = {self}")

        self.wm_title(wm_title)
        self.frm_main = ttk.Frame(self, padding=(10, 10, 10, 10))
        self.frm_main.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.init_layout()

    def init_layout(self):
        self.btn_pose_estimator = ttk.Button(self.frm_main, text="Pose Estimator", command=self.show_pose_estimator, width=50)
        self.btn_pose_estimator.grid(row=0, column=0, sticky="WE")

    def show_pose_estimator(self):
        print("Pose Estimator")
        self.pose_estimator = Pose_Estimator(wm_title="Pose Estimator - Camera", caller=self)
        self.pose_estimator.mainloop()
        # Pose_Estimator(wm_title="Pose Estimator - Camera")

class Pose_Estimator(tk.Tk):
    def __init__(self, wm_title, caller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Pose_Estimator Class = {self}")
        print(f"Pose_Estimator Caller Class = {caller}")

        self.wm_title(wm_title)
        self.frm_main = ttk.Frame(self, padding=(10, 10, 10, 10))
        self.frm_main.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.init_layout()

    def init_layout(self):
        self.cap = cv2.VideoCapture(0)
        self.pTime = 0
        self.detector = poseDetector()

        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 20 # Interval in ms to get the latest frame

        # Create canvas for image
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        # self.canvas.grid(row=0, column=0)
        self.canvas.pack(side=tk.TOP, fill=tk.Y, expand=True)

        # Update image on canvas
        self.update_image()

    def update_image(self):
        # Get the latest frame and convert image format
        img = self.cap.read()[1]
        img = self.detector.findPose(img, draw=True)
        lmList = self.detector.getPosition(img, draw=False)
        cTime = time.time()
        fps = 1/(cTime-self.pTime)
        pTime = cTime
        # self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # to RGB
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format

        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image)

        self.btn_close = ttk.Button(self.frm_main, text="Close", command=self.destroy, width=50)
        self.btn_close.grid(row=0, column=0, sticky="WE")
    
class poseDetector(object):        
    def __init__(
        self, mode=False, upperbody=False, smoothness=True,
        detectConf=0.5, trackConf=0.5
    ):
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

# In[] Run the App
if __name__ == "__main__":
    app = App(wm_title="Pose Estimator - Main")
    app.mainloop()