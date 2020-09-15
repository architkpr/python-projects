import socket
import threading
import argparse


def handle_client(conn, addr):
    welcome_message = "Welcome to the chatroom! Type QUIT to exit."
    exit_message = "You will now be leaving the chatroom. Thank you."
    print("Client {} joined the chatroom!".format(addr[1]))
    conn.send(welcome_message.encode())
    while True:
        message = conn.recv(1024)
        if message.decode() == "QUIT":
            conn.send(exit_message.encode())
            conn.close()
            print("Client {} has left the chatroom.".format(addr[1]))
            break
        else:
            print(str(addr[1]) + ": " + message.decode())


def server_setup(ip, port, clients):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(clients)
    print("Server started at {}:{} with a capacity of {} clients".format(ip, port, clients))
    while True:
        conn, addr = server_socket.accept()
        # Start a new thread for every client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr, ))
        client_thread.start()

    conn.close()
    server_socket.close()


def run_server():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="Enter the IP address of the chatroom server", default="127.0.0.1")
    parser.add_argument("--port", help="Enter the port no. of the chatroom server", default="8001")
    parser.add_argument("--clients", help="Enter the no. of clients to connect to this server", default="5")
    args = parser.parse_args()

    server_setup(args.ip, int(args.port), int(args.clients))


if __name__ == "__main__":
    run_server()
