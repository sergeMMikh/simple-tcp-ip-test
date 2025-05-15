import sys

from clsSocketServer import SocketServer

exit_words = (b'Exit', b'Quit')


def main(host='127.0.0.1', port=9000):
    server = SocketServer(host, port)

    try:
        while True:
            recv_data = server.recv_server_data()
            print(f'Server data input: {recv_data}')

            if recv_data in exit_words:
                break
            else:
                server.send_server_data(recv_data)
    finally:
        server.close()
        print('Exiting')


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9000
    main('127.0.0.1', port)
