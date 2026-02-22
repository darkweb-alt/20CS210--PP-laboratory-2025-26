import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)

print("Server waiting for connection...")
conn, addr = server_socket.accept()
print("Connected from:", addr)

# Receive file data
with open("file.txt", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully.")

conn.close()
server_socket.close()
