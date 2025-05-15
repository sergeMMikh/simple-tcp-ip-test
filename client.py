from clsSocketClient import clsClient
import sys

exit_words = (b'Exit', b'Quit')


def main(host='127.0.0.1', port=9000):
    client = clsClient(host, port)
    while True:
        print('Write your message: ')
        message = input()

        client.send_message(message)

        if message.encode() in exit_words:
            break


if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 9000
    main(host, port)
