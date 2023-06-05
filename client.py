import socket
from tkinter import *

SERVER = '127.0.0.1'
PORT = 1234

def setup():
    global SERVER, PORT
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print('Connected to server')

def musicWindow():
    root = Tk()
    root.mainloop()

if __name__ == '__main__':
    setup()
    musicWindow()
