import socket

PATH = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PATH, PORT))
server.listen(1)

print("Server started...")

conn, addr = server.accept()

print(f"Connect: {addr}")

playerX = True

board = ["?" for _ in range(9)]

while True:
    try:
        data = conn.recv(1024)
        if not data:
            print("Data is not")
            break

        move = int(data.decode()) - 1

        if board[move] == "?":
            board[move] = "X" if playerX else "O"

            conn.send(board[move].encode())
            playerX = not playerX

    except Exception as e:
        print(f"Error: {e}")
        break

server.close()
conn.close()
