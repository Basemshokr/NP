import socket
import threading


def send_message(client_socket):
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break

        # Send the message to the server
        client_socket.sendall(message.encode())


def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server address and port
    client_socket.connect(('localhost', 8888))

    # Start a separate thread for sending messages
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()

    while True:
        # Receive data from the server
        data = client_socket.recv(4096)
        if not data:
            break
        print("Server:", data.decode())

    # Close the connection
    client_socket.close()


start_client()
