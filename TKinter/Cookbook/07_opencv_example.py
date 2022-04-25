# Import required Libraries
from time import sleep
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2, time
from threading import Thread

# Create an instance of TKinter Window or frame
window = tk.Tk()

# Set the size of the window
window.geometry("700x350")# Create a Label to capture the Video frames
label = ttk.Label(window)
label.grid(row=0, column=0)
cap = cv2.VideoCapture(0)


# Define function to show frame
def show_frames():
    frame_rate = 60
    prev = 0
    while True:
        time_elapsed = time.time() - prev
        res, image = cap.read()

        if time_elapsed > 1./frame_rate:
            prev = time.time()

            # Get the latest frame and convert into Image
            cv2image= cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)

            # Convert image to PhotoImage
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image=imgtk)

# Repeat after an interval to capture continiously
# label.after(1, show_frames)

thread_main = Thread(target=show_frames, daemon=True)
thread_main.start()
# show_frames()
window.mainloop()