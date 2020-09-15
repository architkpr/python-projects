import socket
import argparse


def client_setup(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    data = client_socket.recv(1024)
    print(data.decode())
    while True:
        message = input(">")
        client_socket.send(message.encode())
        if message == "QUIT":
            data = client_socket.recv(1024)
            print(data.decode())
            break


def run_client():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="Enter the IP address of the chatroom server", default="127.0.0.1")
    parser.add_argument("--port", help="Enter the port no. of the chatroom server", default="8001")
    args = parser.parse_args()

    client_setup(args.ip, int(args.port))


if __name__ == "__main__":
    run_client()
