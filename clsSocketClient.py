import socket
import time
import os
import locale
from locale import atof


class clsClient:

    def __init__(self, server='127.0.0.1', port=9000):
        self.server = server
        self.port = port


    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            time.sleep(0.01)
            sock.connect((self.server, self.port))
            print(f'Send: {message}')
            sock.sendall(message.encode())
            time.sleep(0.01)
            str_get = sock.recv(16)
            print('Server response <-', str_get)
            sock.close()
