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

board = ["?"] * 9

win_combinations = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def check_winner():
    for (a,b,c) in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "?":
            return board[a]
    if "?" not in board:
        return "Draw"
    return None

while True:
    try:
        data = conn.recv(1024)
        if not data:
            print("Data is not")
            break

        move = int(data.decode()) - 1

        if board[move] == "?":
            board[move] = "X" if playerX else "O"
            winner = check_winner()

            if winner:
                conn.sendall(f"Winner is: {winner}".encode())
                conn.sendall(b"Game Over!")
                break
            else:
                conn.sendall(board[move].encode())
                playerX = not playerX
        else:
            print("Error!")

    except Exception as e:
        print(f"Error: {e}")
        break

server.close()
conn.close()