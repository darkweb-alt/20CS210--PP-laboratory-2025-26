import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

# Send file
with open("file.txt", "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.send(data)

print("File sent successfully.")

client_socket.close()
