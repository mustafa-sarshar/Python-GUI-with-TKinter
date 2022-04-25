# In[] Libs
import sys
import PySimpleGUI as sg

# In[] Vars and Constants

# In[] Design the Layout
layout = [
    [sg.Text(text="Enter the first number:"), sg.Input(key="-IN-NUM-A-")],
    [sg.Text(text="Enter the second number:"), sg.Input(key="-IN-NUM-B-")],
    [sg.Button(button_text="+", key="-BTN-Add-"),
     sg.Button(button_text="-", key="-BTN-Subtract-"),
     sg.Button(button_text="x", key="-BTN-Multiply-"),
     sg.Button(button_text="/", key="-BTN-Divide-")],
    [sg.Text(text="Results: "), sg.Text(text="", key="-OUT-")],
    [sg.Button(button_text="Exit")]
]

# In[] Init the Window
window = sg.Window(title="Simple Calculator", layout=layout)

# In[] Run the App
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit", sg.WIN_CLOSED):
        break
    # Catch operators
    try:
        num_a, num_b = int(values["-IN-NUM-A-"]), int(values["-IN-NUM-B-"])
        if event == "-BTN-Add-":
            res_output = f"{num_a} + {num_b} = {num_a + num_b}"
        elif event == "-BTN-Subtract-":
            res_output = f"{num_a} - {num_b} = {num_a - num_b}"
        elif event == "-BTN-Multiply-":
            res_output = f"{num_a} x {num_b} = {num_a * num_b}"
        elif event == "-BTN-Divide-":
            res_output = f"{num_a} / {num_b} = {(num_a / num_b):0.2f}"
    except BaseException as error:
        res_output = repr(error)
        window["-OUT-"].update(res_output)
    else:
        window["-OUT-"].update(res_output)

window.close()
