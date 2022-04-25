"""
Inspired by (accessed on 01.11.21):
    https://realpython.com/python-gui-tkinter/#working-with-widgets    
"""
# In[] Libs
import tkinter as tk
from tkinter import messagebox

# In[] List of field labels
labels = [
    "First Name",
    "Last Name",
    "Address Line 1",
    "Address Line 2",
    "City",
    "State/Province",
    "Postal Code",
    "Country",
]

labels_list = []
entry_list = []

# In[] Functions
def form_submit():
    msg = ""
    for idx, text in enumerate(labels):
        if entry_list[idx].get() != "":
            msg = msg + labels[idx] + ": " + entry_list[idx].get() + "\n"
    
    messagebox.showinfo(title="Submitted", message=msg)

def form_clear():
    for idx, text in enumerate(labels):
        entry_list[idx].delete(0, tk.END)

# In[] Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

# In[] Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack()

# Loop over the list of field labels
for idx, text in enumerate(labels):
    # Create a Label widget with the text from the labels list
    labels_list.append(tk.Label(master=frm_form, text=text+":"))
    # Create an Entry widget
    entry_list.append(tk.Entry(master=frm_form, width=50))
    # Use the grid geometry manager to place the Label and
    # Entry widgets in the row whose index is idx
    labels_list[idx].grid(row=idx, column=0, sticky="e")
    entry_list[idx].grid(row=idx, column=1)

# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Submit", command=form_submit)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear", command=form_clear)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

# Start the application
window.mainloop()