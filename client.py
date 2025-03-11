import socket

PATH = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((PATH, PORT))

print("Client started...")

res = 5

client.send(str(res).encode())

client.close()