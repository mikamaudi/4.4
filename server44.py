import socket
from protocolHelper import Protocol
class Server44:
    def __init__(self):
        self.server_socket = socket.socket()
        self.server_socket.bind(('0.0.0.0', 80))
        self.server_socket.listen()

    def loop(self):
        print("server is up and running")

        (client_socket, client_address) = self.server_socket.accept()

        msg, headers, data = Protocol.get_msg(client_socket)
        print(msg)
        print(headers)
        print(data)

        client_socket.close()
        server_data = " "

if __name__== "__main__":
    my_server = Server44()
    while True:
        my_server.loop()
    my_server.close()
