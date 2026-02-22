# ---------------------------------------------------------
# Client Program for TCP Communication
# ---------------------------------------------------------

# Importing socket module
import socket

# Create a socket object using IPv4 and TCP protocol
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
host = "127.0.0.1"   # Localhost
port = 5000          # Same port as server

# Connect to the server
client_socket.connect((host, port))

# Send message to server
message = "Hello Server!"
client_socket.send(message.encode())

# Receive response from server
response = client_socket.recv(1024).decode()
print("Message received from server:", response)

# Close the connection
client_socket.close()