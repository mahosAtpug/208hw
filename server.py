import socket
import threading

SERVER = '127.0.0.1'
IP_ADDRESS = '127.0.0.1'
PORT = 1234
Clients = {}

def setup():
    global SERVER, IP_ADDRESS, PORT, server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP_ADDRESS, PORT))
    server.listen(100)
    print('Server started. Listening on {}:{}'.format(IP_ADDRESS, PORT))

    while True:
        client, address = server.accept()
        Clients[client] = address
        print('New connection from {}'.format(address))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

def handle_client(client):
    while True:
        pass

def acceptConnections():
    while True:
        client, address = server.accept()
        Clients[client] = address
        print('New connection from {}'.format(address))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    setup()