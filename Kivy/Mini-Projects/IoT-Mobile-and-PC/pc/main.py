import matplotlib.pyplot as plt
import socket

def listen_once():
    # Get host from Wireless LAN Adapter wi-fi ipv4
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 65436

    print(f"Listen on {HOST}: {PORT}")

    data_to_plot = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()
        fig = plt.figure()
        with conn:
            print(f"Connected by client with IP Address {addr}")
            while True:
                data = sock.recv(1024)
                if data.decode() != "":
                    data = data.decode("utf-8")
                    print(data)
                    data_to_plot.append(int(data))
                    plt.pause(.2)

if __name__ == "__main__":
    listen_once()