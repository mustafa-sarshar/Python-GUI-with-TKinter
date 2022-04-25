# Source: https://www.youtube.com/watch?v=uv8PciALzSI&t=70s&ab_channel=ErikSandberg

import matplotlib.pyplot as plt
import socket

def listen_once():
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 65436
    print(f"Listening on: {SERVER_IP}:{SERVER_PORT}")

    list_data = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
        sckt.bind((SERVER_IP, SERVER_PORT))
        sckt.listen()
        conn, addr = sckt.accept()
        fig = plt.figure()
        with conn:
            print(f"Connect by client with ip address: {addr}")
            while True:
                data = conn.recv(1034)
                if data.decode() != "":
                    data = data.decode("utf-8")
                    print(data)
                    list_data.append(float(data))
                    timeline = list(range(len(list_data)))
                    plt.plot(timeline, list_data, 'b-')
                    plt.pause(.2)

if __name__ == "__main__":
    listen_once()