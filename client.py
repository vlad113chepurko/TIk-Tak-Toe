import socket
from tkinter import *

PATH = "127.0.0.1"
PORT = 12345

root = Tk()
root.geometry("500x500")
root.title("Tic Tak Toe")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((PATH, PORT))

print("Client started...")

btn1 = Button(root, text="?", bg="orange", font=("Arial", 30))
btn2 = Button(root, text="?", bg="orange", font=("Arial", 30))
btn3 = Button(root, text="?", bg="orange", font=("Arial", 30))

btn4 = Button(root, text="?", bg="orange", font=("Arial", 30))
btn5 = Button(root, text="?", bg="orange", font=("Arial", 30))
btn6 = Button(root, text="?", bg="orange", font=("Arial", 30))

btn7 = Button(root, text="?", bg="orange", font=("Arial", 30))
btn8 = Button(root, text="?", bg="orange", font=("Arial", 30))
btn9 = Button(root, text="?", bg="orange", font=("Arial", 30))

btn1.grid(column=1, row=1)
btn2.grid(column=2, row=1)
btn3.grid(column=3, row=1)
btn4.grid(column=1, row=2)
btn5.grid(column=2, row=2)
btn6.grid(column=3, row=2)
btn7.grid(column=1, row=3)
btn8.grid(column=2, row=3)
btn9.grid(column=3, row=3)

res = 5

client.send(str(res).encode())

client.close()
root.mainloop()