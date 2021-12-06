# In[] Libs
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from threading import Thread
from queue import Queue
from time import sleep
from queues import write_to_scrolled_text
import sys
from os import path, makedirs
from pathlib import Path

# In[] Define the App Class
class App(object):
    def __init__(self, title):
        # Define the Layout and Widgets
        self.window = tk.Tk()
        self.window.wm_title(title)
        self.window.resizable(True, True)

        self.tab_controller = ttk.Notebook(master=self.window)
        self.tab_controller.pack(fill=tk.BOTH, expand=True)

        self.frm_tab_1 = ttk.Frame(master=self.tab_controller)
        self.frm_tab_2 = ttk.Frame(master=self.tab_controller)
        self.tab_controller.add(child=self.frm_tab_1, text="Text Updater")
        self.tab_controller.add(child=self.frm_tab_2, text="Manage Files")

        # Define Vars
        self.var_fontsize = tk.IntVar(master=self.frm_tab_1, value=10)
        self.var_txt_input = tk.StringVar(master=self.frm_tab_1, value="")
        self.var_update_output = tk.BooleanVar(master=self.frm_tab_1, value=False)
        self.var_filename = tk.StringVar(self.frm_tab_2, value="")
        self.var_copyto_dir = tk.StringVar(self.frm_tab_2, value="")

        # Tab - Text Updater *****************************************
        lbl_input = ttk.Label(master=self.frm_tab_1, text="Input Text:")
        lbl_input.grid(row=0, column=0, sticky="W")
        self.ent_input = ttk.Entry(master=self.frm_tab_1, width=60, textvariable=self.var_txt_input)
        self.ent_input.grid(row=1, column=0, columnspan=2, sticky="W")

        self.lbl_output = ttk.Label(master=self.frm_tab_1, text="Output:")
        self.lbl_output.grid(row=2, column=0, sticky="W")
        self.scrtext_output = scrolledtext.ScrolledText(master=self.frm_tab_1, width=45, height=10, wrap=tk.WORD, font=("Arial", self.var_fontsize.get()))
        self.scrtext_output.grid(row=3, column=0, columnspan=2)
        self.lbl_fontsize = ttk.Label(master=self.frm_tab_1, text="Font size:")
        self.lbl_fontsize.grid(row=4, column=0, sticky="W")
        self.spin_fontsize = tk.Spinbox(master=self.frm_tab_1, from_=10, to=30, width=5, bd=8, command=self._spin, textvariable=self.var_fontsize)
        self.spin_fontsize.grid(row=4, column=1, sticky="W")
        self.chk_update_output = ttk.Checkbutton(master=self.frm_tab_1, text="Update Output", variable=self.var_update_output, offvalue=False, onvalue=True)
        self.chk_update_output.grid(row=5, column=0, sticky="W")

        # self.btn_show_queue = ttk.Button(master=self.frm_tab_1, text="Show the Queued Message", command=lambda: self.create_thread(num_of_queues_to_show=2))
        self.btn_show_queue = ttk.Button(master=self.frm_tab_1, text="Show the Queued Message", command=lambda: write_to_scrolled_text(self, n_q_to_show=2))
        self.btn_show_queue.grid(row=6, column=0, sticky="W")

        # Tab - Manage Files *****************************************
        self.btn_open_file = ttk.Button(master=self.frm_tab_2, text="Open Source File", command=self.show_open_file_window)
        self.btn_open_file.grid(row=0, column=0, sticky="E")
        self.ent_filename = ttk.Entry(master=self.frm_tab_2, width=50, textvariable=self.var_filename, state="readonly")
        self.ent_filename.grid(row=0, column=1, sticky="W")
        self.btn_open_copyto_dir = ttk.Button(master=self.frm_tab_2, text="Open Destination Dir", command=self.show_open_dir_window)
        self.btn_open_copyto_dir.grid(row=1, column=0, sticky="E")
        self.ent_copyto_dir = ttk.Entry(master=self.frm_tab_2, width=50, textvariable=self.var_copyto_dir, state="readonly")
        self.ent_copyto_dir.grid(row=1, column=1, sticky="W")
        self.btn_copy_file = ttk.Button(master=self.frm_tab_2, text="Copy", command=self.copy_file, state="disabled")
        self.btn_copy_file.grid(row=2, column=0, columnspan=2, sticky="E")

        self.scrtext_output.bind("<<Modified>>", self.changed_scrtext)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing_app)
        self.create_queues()
        self.tab_controller.select(1)
        print(self.btn_open_copyto_dir["state"])

    def _spin(self):
        self.scrtext_output.configure(font=("Arial", self.var_fontsize.get()))
        print(f"Font size: {self.var_fontsize.get()}")

    def changed_scrtext(self, *args):
        self.scrtext_output.see(tk.END)
        self.scrtext_output.edit_modified(0)

    def update_output(self, sleep_sec):
        while self.var_update_output.get():
            sleep(sleep_sec)
            print(f"Text Input: {self.var_txt_input.get()}")
            if self.var_txt_input.get() != "":
                self.scrtext_output.insert(index=tk.INSERT, chars=f"After {sleep_sec} sec. -> {self.var_txt_input.get()}\n")
            print(f"Thread sleeps for {sleep_sec}")

    # Create Queue instance
    def create_queues(self):
        self.guiQueue = Queue()
        print(self.guiQueue)
        for idx in range(10):
            self.guiQueue.put(f"Message from queue: {idx}")
    
    def create_thread(self, num_of_queues_to_show):
        thread = Thread(target=self.show_queues, args=[num_of_queues_to_show])
        thread.run()
    
    def show_queues(self, num_of_queues_to_show):
        for queue in range(num_of_queues_to_show):
            sleep(1)
            print(f"Loop No. {queue}: -> {self.guiQueue.get()}")

    def show_open_file_window(self):
        fname = filedialog.askopenfilename(
            initialdir="",
            title="Select a file please...",
            filetypes=(("Any File Type", "*.*"), )
        )
        self.var_filename.set(fname)
        self.copy_file_situation()

    def show_open_dir_window(self):
        path_dir = filedialog.askdirectory(
            initialdir=Path(path.dirname(__file__), "copy_directory"),
            title="Select the destination directory",
        )
        self.var_copyto_dir.set(path_dir)
        self.copy_file_situation()

    def copy_file_situation(self):
        if self.var_copyto_dir.get() and self.var_filename.get(): self.btn_copy_file.configure(state="normal")
        else: self.btn_copy_file.configure(state="disabled")

    def copy_file(self):
        import shutil # Shutil is short-hand notation for shell utility
        src = Path(self.ent_filename.get())
        dst = Path(self.ent_copyto_dir.get(), src.name)
        try:
            shutil.copy(src, dst)
            messagebox.showinfo("Copy File to Network", f"Success:\n{Path(self.var_filename.get()).name} -- copied to --> \n{self.var_copyto_dir.get()}")
        except FileNotFoundError as err:
            messagebox.showerror("Copy File to Network", "*** Failed to copy file! ***\n\n" + str(err))
        except Exception as ex:
            messagebox.showerror("Copy File to Network", "*** Failed to copy file! ***\n\n" + str(ex))

    @staticmethod
    def create_copy_directory():
        _dir_path = path.dirname(__file__)
        _dir_path = Path(_dir_path, "copy_directory")
        if not path.exists(_dir_path):
            makedirs(_dir_path, exist_ok=True)

    def on_closing_app(self):
        self.window.quit()
        self.window.destroy()
        sys.exit()

    def run(self):
        self.create_copy_directory()
        self.thread_1 = Thread(target=self.update_output, args=[1], daemon=True)
        self.thread_1.start()
        self.thread_2 = Thread(target=self.update_output, args=[2], daemon=True)
        self.thread_2.start()
        self.window.mainloop()

# In[] Run the App
if __name__ == "__main__":
    app = App("Thread and Networking Example")
    app.run()