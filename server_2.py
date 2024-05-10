import socket

# Broadcast server
def broadcast_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the server address and port
    server_address = ('', 5555)
    server_socket.bind(server_address)

    print("Broadcast server is running...")

    clients = set()  # Store clients' addresses

    while True:
        # Receive message from any client
        data, client_address = server_socket.recvfrom(4096)
        print(f"Received message from {client_address}: {data.decode()}")

        # Add the client to the set of clients
        clients.add(client_address)

        # Broadcast the message to all clients except the sender
        for client in clients:
            if client != client_address:
                server_socket.sendto(data, client)

    server_socket.close()

# Start the broadcast server
broadcast_server()
