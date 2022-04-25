# In[] Libs
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# In[] Functions and Methods
def click_me():
    print(lbl_click_me["foreground"])
    if lbl_click_me["foreground"] == "black" or lbl_click_me["foreground"] == "green":
        lbl_click_me.configure(foreground="red", text="Fill in the form below!!!")
        btn_click_me.configure(text="Clicked!")
    else:
        lbl_click_me.configure(foreground="green", text="Heyyyy!!!!")
        btn_click_me.configure(text="Click Me Again!")

def show_info():
    msg_1 = ""
    if var_gender.get() == "female": msg_1 = " Mrs."
    elif var_gender.get() == "male": msg_1 = " Mr."
    msg_2 = var_nationality.get()
    msg_3 = "but not a student"
    if var_student.get() == True: msg_3 = "and a student"
    msg = f"Dear{msg_1} {var_name.get()}\nYou are from {msg_2} {msg_3}!"
    messagebox.showinfo(title="Info!", message=msg)

def _exit():
    window.quit()
    window.destroy()
    exit()

# In[] Define the Layout and Widgets
window = tk.Tk()
window.wm_title("Python Simple App")
window.resizable(True, True)

menu_bar = tk.Menu(master=window)

menu_file = tk.Menu(master=menu_bar, tearoff=False)
menu_file.add_command(label="New")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=_exit)
menu_bar.add_cascade(label="File", menu=menu_file)

menu_help = tk.Menu(master=menu_bar, tearoff=False)
menu_help.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=menu_help)

lbl_click_me = ttk.Label(master=window, text="Click the 'Click Me' button!", foreground="black")
lbl_click_me.grid(row=0, column=0)
btn_click_me = ttk.Button(master=window, text="Click Me!", command=click_me)
btn_click_me.grid(row=0, column=1)

lblfrm_contact_info = ttk.LabelFrame(master=window, text="Contact Info")
lblfrm_contact_info.grid(row=1, column=0, columnspan=3)

lbl_name = ttk.Label(master=lblfrm_contact_info, text="Enter a name:", foreground="black")
lbl_name.grid(row=0, column=0)
var_name = tk.StringVar(value="Your Name")
ent_name = ttk.Entry(master=lblfrm_contact_info, textvariable=var_name)
ent_name.grid(row=1, column=0)

lbl_gender = ttk.Label(master=lblfrm_contact_info, text="Gender:")
lbl_gender.grid(row=0, column=1)
var_gender = tk.StringVar()
cmb_gender = ttk.Combobox(master=lblfrm_contact_info, width=12, textvariable=var_gender, state="readonly")
cmb_gender["values"] = ["male", "female", "diverse"]
cmb_gender.current(0)
cmb_gender.grid(row=1, column=1)

var_student = tk.BooleanVar(value=False)
chk_student = ttk.Checkbutton(master=lblfrm_contact_info, text="student", variable=var_student, offvalue=False, onvalue=True)
chk_student.grid(row=1, column=2)

var_nationality = tk.StringVar(value="U.S")
rad_nationality = ttk.Radiobutton(master=lblfrm_contact_info, text="U.S", variable=var_nationality, value="U.S")
rad_nationality.grid(row=0, column=3, sticky="W")
rad_nationality = ttk.Radiobutton(master=lblfrm_contact_info, text="Non-U.S", variable=var_nationality, value="non-U.S")
rad_nationality.grid(row=1, column=3, sticky="W")

lblfrm_bio = ttk.LabelFrame(master=window, text="Bio:")
lblfrm_bio.grid(row=2, column=0, columnspan=4, sticky="WE")
srltxt_bio = scrolledtext.ScrolledText(master=lblfrm_bio, width=40, height=5, wrap=tk.WORD)
srltxt_bio.grid(row=0, column=0, columnspan=4, sticky="WE")

btn_info = ttk.Button(master=window, text="Show Info", command=show_info)
btn_info.grid(row=3, column=2, sticky="E")

ent_name.focus()

print(window.winfo_children())
for widget in window.winfo_children():
    if widget is not menu_bar: widget.grid_configure(padx=3, pady=3)

window.configure(menu=menu_bar)
window.mainloop()
