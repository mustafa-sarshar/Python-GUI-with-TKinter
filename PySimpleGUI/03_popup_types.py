# In[] Libs
import sys
import os
import PySimpleGUI as sg

# In[] Vars and Constants
LIST_POPUPS = [
    "popup",
    "popup_no_border",
    "popup_no_frame",
    "popup_get_text",
    "popup_get_folder",
    "popup_get_file",
    "popup_no_wait" ,
    "popup_animated",
    "popup_cancel"
]
LIST_MESSAGES = [
    "",
    "",
    "",
    "Write a text",
    "Browse a folder",
    "Browse a file",
    "",
    "popup_animated",
    "popup_cancel"
]

if len(sys.argv) > 1:
    list_popups_index = int(sys.argv[1])
else:
    list_popups_index = 0
AUTO_CLOSE = True
AUTO_CLOSE_DURATION = 10 # seconds

# In[] Design the Layout
layout = [
    [sg.Text(text="See all types of Popup", justification="center")],
    [sg.Text(text=f"Popup type: '{LIST_POPUPS[list_popups_index]}'", key="-TXT-TYPES-", text_color="yellow", justification="center")],
    [sg.Button(button_text="Let`s Start", key="-BTN-GO-", bind_return_key=True)]
]

# In[] Init the Window
window = sg.Window(title="Popup Types", layout=layout)

# In[] Run the App
while True:
    print(LIST_POPUPS[list_popups_index])
    event, values = window.read(close=False)  # change close parameter to True for one-shot window    
    print(event, values)
    
    if event in (None, "Exit", sg.WIN_CLOSED):
        sg.popup_auto_close("Bye bye...")
        break
    
    if LIST_POPUPS[list_popups_index] == "popup":
        r = sg.popup(title=f"Type: {LIST_POPUPS[list_popups_index]}", auto_close=AUTO_CLOSE, auto_close_duration=AUTO_CLOSE_DURATION)
        sg.popup_no_border(f"Returned value: {r}")
        
    elif LIST_POPUPS[list_popups_index] == "popup_no_border":
        r = sg.popup_no_border(auto_close=AUTO_CLOSE, auto_close_duration=AUTO_CLOSE_DURATION)
        sg.popup_no_border(f"Returned value: {r}")
    
    elif LIST_POPUPS[list_popups_index] == "popup_no_border":
        r = sg.popup_no_frame(auto_close=AUTO_CLOSE, auto_close_duration=AUTO_CLOSE_DURATION)
        sg.popup_no_border(f"Returned value: {r}")
    
    elif LIST_POPUPS[list_popups_index] == "popup_get_text":
        r = sg.popup_get_text(title=f"Type: {LIST_POPUPS[list_popups_index]}", message=LIST_MESSAGES[list_popups_index])
        sg.popup_no_border(f"Returned value: {r}")
        
    elif LIST_POPUPS[list_popups_index] == "popup_get_folder":
        r = sg.popup_get_folder(title=f"Type: {LIST_POPUPS[list_popups_index]}", message=LIST_MESSAGES[list_popups_index])
        sg.popup_scrolled(title="All files inside the folder", *os.listdir(r))
        
    elif LIST_POPUPS[list_popups_index] == "popup_get_file":
        r = sg.popup_get_file(title=f"Type: {LIST_POPUPS[list_popups_index]}", message=LIST_MESSAGES[list_popups_index], file_types=(("ALL Files", ". *"),))
        sg.popup_no_border(f"Returned value: {r}")
        
    elif LIST_POPUPS[list_popups_index] == "popup_no_wait":
        r = sg.popup_no_wait(title=f"Type: {LIST_POPUPS[list_popups_index]}", auto_close=AUTO_CLOSE, auto_close_duration=AUTO_CLOSE_DURATION)
        sg.popup_no_border(f"Returned value: {r}")
    
    elif LIST_POPUPS[list_popups_index] == "popup_animated":
        r = sg.popup_animated(image_source="files/animation.gif", message=LIST_MESSAGES[list_popups_index], time_between_frames=1)
        sg.popup_no_border(f"Returned value: {r}")
    
    elif LIST_POPUPS[list_popups_index] == "popup_cancel":
        sg.popup_cancel(title=f"Type: {LIST_POPUPS[list_popups_index]}")
        sys.exit()
        
    print(LIST_POPUPS[list_popups_index])
    
    if list_popups_index < len(LIST_POPUPS) - 1:        
        list_popups_index += 1
    else:
        list_popups_index = 0
        
    window["-TXT-TYPES-"].update(f"Let`s Start with '{LIST_POPUPS[list_popups_index]}'")
window.close()

