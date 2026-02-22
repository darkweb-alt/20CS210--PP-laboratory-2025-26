# ---------------------------------------------------------
# Server Program for TCP Communication
# ---------------------------------------------------------
# Importing socket module
import socket
# Create a socket object using IPv4 and TCP protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to host and port number
host = "127.0.0.1"     # Localhost
port = 5000            # Port number
server_socket.bind((host, port))
# Listen for incoming client connections
server_socket.listen(1)
print("Server is waiting for connection...")
# Accept the connection from client
client_socket, address = server_socket.accept()
print("Connection established with:", address)
# Receive message from client
message = client_socket.recv(1024).decode()
print("Message received from client:", message)
# Send response back to client
response = "Hello Client, Message received!"
client_socket.send(response.encode())
# Close the connection
client_socket.close()
server_socket.close()