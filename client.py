from clsSocketClient import clsClient

exit_words = (b'Exit', b'Quit')


def main():
    client = clsClient(port=9000)
    while True:
        print('Write your message: ')
        message = input()

        client.send_message(message)

        if message.encode() in exit_words:
            break


if __name__ == "__main__":
    main()
