import socket
from tkinter import *

PATH = "127.0.0.1"
PORT = 5000

root = Tk()
root.geometry("500x500")
root.title("Tic Tak Toe")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((PATH, PORT))

label = Label(text="Winner will be here.")

print("Client started...")

def handle_button(resp, btn):
    client.send(str(resp).encode())

    server_resp = client.recv(1024).decode()

    if "Winner" in server_resp:
        print(server_resp)
        label.config(text=server_resp)
    elif server_resp == "Game Over":
        print("Game Over")
        label.config(text="Game Over")
    elif server_resp == "Invalid move":
        print("Invalid move, try again.")
    else:
        btn.config(text=server_resp)




btn1 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(1, btn1))
btn2 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(2, btn2))
btn3 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(3, btn3))

btn4 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(4, btn4))
btn5 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(5, btn5))
btn6 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(6, btn6))

btn7 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(7, btn7))
btn8 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(8, btn8))
btn9 = Button(root, text="?", bg="orange", font=("Arial", 30), command=lambda: handle_button(9, btn9))

btn1.grid(column=1, row=1)
btn2.grid(column=2, row=1)
btn3.grid(column=3, row=1)
btn4.grid(column=1, row=2)
btn5.grid(column=2, row=2)
btn6.grid(column=3, row=2)
btn7.grid(column=1, row=3)
btn8.grid(column=2, row=3)
btn9.grid(column=3, row=3)

root.mainloop()