import socket

# Broadcast client
def broadcast_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set the socket to allow broadcasting
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send messages
    while True:
        message = input("Enter message to broadcast: ")
        client_socket.sendto(message.encode(), ('<broadcast>', 5555))

    client_socket.close()

# Start the broadcast client
broadcast_client()
