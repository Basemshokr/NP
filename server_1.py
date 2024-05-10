import socket
import threading


def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(4096)
        if not data:
            break
        print("[Received]", data.decode())

        # Echo back the received message to the client
        client_socket.sendall(data)

    # Close the connection
    client_socket.close()


def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind(('localhost', 8888))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server is listening on port 8888...")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print("Connected to", client_address)

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


start_server()
