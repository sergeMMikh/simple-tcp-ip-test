from clsSocketServer import SocketServer

exit_words = (b'Exit', b'Quit')


def main():
    server = SocketServer(port=9000)

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
    main()
