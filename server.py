import socket
from tkinter import *

PATH = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PATH, PORT))
server.listen(1)

print("Server started....")

conn, addr = server.accept()

print(f"{addr}")

while True:
    try:
        data = conn.recv(1024)
        if not data:
            print("Data is not")
            break
        print(f"Data: {data}")
    except Exception as e:
        print(f"Error: {e}")

server.close()
conn.close()