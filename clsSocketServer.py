import socket
import select


# http://theembeddedlab.com/tutorials/simple-socket-server-python/

class SocketServer:
    """ Simple socket server that listens to one single client. """

    def __init__(self, host='0.0.0.0', port=9000):
        """ Initialize the server with a host and port to listen to. """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = host
        self.port = port
        self.sock.bind((host, port))
        self.sock.listen(1)

    def close(self):
        """ Close the server socket. """
        print('Closing server socket (host {}, port {})'.format(self.host, self.port))
        if self.sock:
            self.sock.close()
            self.sock = None

    def run_server(self, message):
        """ Accept and handle an incoming connection. """
        print('Starting socket server (host {}, port {})'.format(self.host, self.port))

        self.client_sock, self.client_addr = self.sock.accept()

        print('Client {} connected'.format(self.client_addr))

        stop = False
        while not stop:
            if self.client_sock:
                # Check if the client is still connected and if data is available:
                try:
                    rdy_read, rdy_write, sock_err = select.select([self.client_sock, ], [], [])
                except select.error:
                    print('Select() failed on socket with {}'.format(self.client_addr))
                    return 1

                if len(rdy_read) > 0:
                    read_data = self.client_sock.recv(255)
                    # Check if socket has been closed
                    if len(read_data) == 0:
                        print('{} closed the socket.'.format(self.client_addr))
                        stop = True
                    else:
                        print('>>> Received: {}'.format(read_data.rstrip()))
                        if read_data.rstrip() == 'quit':
                            stop = True
                        else:
                            self.client_sock.send(message.encode())
            else:
                print("No client is connected, SocketServer can't receive data")
                stop = True

        # Close socket
        print('Closing connection with {}'.format(self.client_addr))
        self.client_sock.close()
        return 0

    def recv_server_data(self):
        """ Accept and handle an incoming connection. """
        print('Starting socket server (host {}, port {})'.format(self.host, self.port))

        self.client_sock, self.client_addr = self.sock.accept()

        print('Client {} connected'.format(self.client_addr))

        read_data = str()

        stop = False
        while not stop:
            if self.client_sock:
                # Check if the client is still connected and if data is available:
                try:
                    rdy_read, rdy_write, sock_err = select.select([self.client_sock, ], [], [])
                except select.error:
                    print('Select() failed on socket with {}'.format(self.client_addr))
                    return 1

                if len(rdy_read) > 0:
                    read_data = self.client_sock.recv(1024)
                    # Check if socket has been closed
                    if len(read_data) == 0:
                        print('{} closed the socket.'.format(self.client_addr))
                        stop = True
                    else:
                        print('>>> Received: {}'.format(read_data.rstrip()))
                        stop = True
            else:
                print("No client is connected, SocketServer can't receive data")
                stop = True
                # Close socket
                print('Closing connection with {}'.format(self.client_addr))
                self.client_sock.close()

        return read_data

    def send_server_data(self, message):
        """Send a message to the connected client."""
        if self.client_sock:
            if isinstance(message, str):
                message = message.encode()
            self.client_sock.sendall(message)
            print(f'Sent: {message}')
            print(f'Closing connection with {self.client_addr}')
            self.client_sock.close()
            self.client_sock = None
        else:
            print('No client to send data to.')

    def send_str_server_data(self, message):
        print('M_data', message)
        self.client_sock.send(message.encode())
        # Close socket
        print('Closing connection with {}'.format(self.client_addr))
        self.client_sock.close()
        return 0
