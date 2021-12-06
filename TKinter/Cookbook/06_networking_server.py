"""
This Tutorial inspired by:
    - sentdex: https://www.youtube.com/watch?v=CV7_stUWvBQ
"""
# In[] Libs
import socket
import select
from socketserver import BaseRequestHandler, TCPServer
from threading import Thread
import tkinter as tk
from tkinter import ttk, scrolledtext
from time import sleep
from queue import Queue

# In[] Define Objects
class RequestHandler(BaseRequestHandler):
    # override base class handle method
    def handle(self):
        print("Server connected to: ", self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp: break
            self.request.send(b"Server received: {rsp}")

# In[] Design the Layout
class App:
    def __init__(self, title=""):
        self.window = tk.Tk()
        self.window.wm_title(title)

        self.lblfrm_msg_to_clients = ttk.LabelFrame(master=self.window, text="Server: send message to clients")
        self.lblfrm_msg_to_clients.pack(pady=10, padx=10)
        self.lblfrm_msg_from_clients = ttk.LabelFrame(master=self.window, text="Server: messages from clients")
        self.lblfrm_msg_from_clients.pack(pady=10, padx=10)
        self.btn_run_the_server = ttk.Button(master=self.window, text="Run the server", command=self.run_the_server)
        self.btn_run_the_server.pack(pady=10, padx=10)

        # Init the App
        self.init_variables()
        self.add_widgets()

    def init_variables(self):
        self.var_msg_to_clients = tk.StringVar(master=self.lblfrm_msg_to_clients, value="")
        self.queue_messages = Queue()
        self.update_messages = "MSG"

    def add_widgets(self):
        self.ent_msg_to_clients = ttk.Entry(master=self.lblfrm_msg_to_clients, textvariable=self.var_msg_to_clients, width=55)
        self.ent_msg_to_clients.pack(side=tk.LEFT)
        self.btn_send_msg_to_clients = ttk.Button(master=self.lblfrm_msg_to_clients, text="Send")
        self.btn_send_msg_to_clients.pack(side=tk.RIGHT)
        self.scrtext_msg_from_clients = scrolledtext.ScrolledText(master=self.lblfrm_msg_from_clients, width=50, height=5, wrap=tk.WORD)
        self.scrtext_msg_from_clients.pack(side=tk.LEFT)

        self.scrtext_msg_from_clients.bind("<<Modified>>", self._changed_scrtext)

    def _changed_scrtext(self, *args):
        self.scrtext_msg_from_clients.see(tk.END)
        self.scrtext_msg_from_clients.edit_modified(0)

    def update_output(self):
        while True:
            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list)
            for notified_socket in read_sockets:
                if notified_socket == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    user = self.receive_message(client_socket)
                    if user is False:
                        continue
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user
                    print("Accepted new connection from {}:{}, username: {}".format(*client_address, user["data"].decode("utf-8")))
                else:
                    message = self.receive_message(notified_socket)
                    if message is False:
                        print("Closed connection from: {}".format(self.clients[notified_socket]["data"].decode("utf-8")))
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue
                    user = self.clients[notified_socket]
                    print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

                    # Iterate over connected clients and broadcast message
                    for client_socket in self.clients:
                        # But don't sent it to sender
                        if client_socket != notified_socket:
                            # Send user and message (both with their headers)
                            # We are reusing here message header sent by sender, and saved username header send by user when he connected
                            client_socket.send(user["header"] + user["data"] + message["header"] + message["data"])
            # It's not really necessary to have this, but will handle some socket exceptions just in case
            for notified_socket in exception_sockets:
                # Remove from list for socket.socket()
                self.sockets_list.remove(notified_socket)
                # Remove from our list of users
                del self.clients[notified_socket]
            # update_message = ""
            # self.scrtext_msg_from_clients.insert(index=tk.INSERT, chars=update_message+"\n")

    def establish_the_server(self):
        self.HEADER_LENGTH = 10
        self.IP = "127.0.0.1"
        self.PORT = 1234
        
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.IP, self.PORT))
        self.server_socket.listen()
        self.sockets_list = [self.server_socket]
        self.clients = {}
        self.update_output()

        # self.con_server = TCPServer(server_address=("localhost", 5555), RequestHandlerClass=RequestHandler) # set the Server to localhost or 127.0.0.1
        # self.con_server.serve_forever()

    def run_the_server(self):
        self.thread_update_messages = Thread(target=self.establish_the_server, daemon=True)
        self.thread_update_messages.run()

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH)
            if not len(message_header):
                return False # No message is received
            message_length = int(message_header.decode("utf-8").strip())
            return dict(
                header=message_header,
                data=client_socket.recv(message_length)
            )
        except:
            return False

    def run(self):
        # w, h = 300, 300
        # self.window.geometry(f"{w}x{h}")
        self.run_the_server()
        self.window.mainloop()

# In[] Run the App
if __name__ == "__main__":
    app = App(title="Server")
    app.run()