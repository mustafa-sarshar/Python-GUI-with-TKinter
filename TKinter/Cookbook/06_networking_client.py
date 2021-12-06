# In[] Libs
from socket import socket, AF_INET, SOCK_STREAM
import tkinter as tk
from tkinter import ttk

# In[] Define Functions

class App:
    def __init__(self, title=""):
        self.window = tk.Tk()
        self.window.wm_title(title)

        self.lblfrm_msg_to_server = ttk.LabelFrame(master=self.window, text="Server: send message to server")
        self.lblfrm_msg_to_server.pack(pady=10, padx=10)

        # Init the App
        self.init_variables()
        self.add_widgets()

    def init_variables(self):
        self.var_msg_to_server = tk.StringVar(master=self.lblfrm_msg_to_server, value="")

    def add_widgets(self):
        self.ent_msg_to_server = ttk.Entry(master=self.lblfrm_msg_to_server, textvariable=self.var_msg_to_server, width=55)
        self.ent_msg_to_server.pack(side=tk.LEFT)
        self.btn_send_msg_to_server = ttk.Button(master=self.lblfrm_msg_to_server, text="Send", command=self.send_msg_to_server)
        self.btn_send_msg_to_server.pack(side=tk.RIGHT)

    def send_msg_to_server(self):
        if self.var_msg_to_server.get():
            self.con_socket.send(bytes(self.var_msg_to_server.get().encode()))
    
    def connect_to_server(self):
        self.con_socket = socket(family=AF_INET, type=SOCK_STREAM)
        self.con_socket.connect(("localhost", 5555))
        
    def run(self):
        self.connect_to_server()
        w, h = 300, 300
        self.window.geometry(f"{w}x{h}")
        self.window.mainloop()

# In[] Run the App
if __name__ == "__main__":
    client_name = input("Write you name: ")
    app = App(title=f"Client - {client_name}")
    app.run()
