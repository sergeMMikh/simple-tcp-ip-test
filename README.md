# A Simple TCP/IP Learning Tool for Students

This tool starts a basic local echo server using the command:
``` bash
python3 ./server.py
```

To run the client, use:
```bash
python3 ./client.py
```

The default server address is 127.0.0.1, and the default port is 9000.

Also it's possible to define some arguments for:
 - server: `python3 ./server.py <port number>`
 - client: `python3 ./client.py <sderver> <port number>`

example:
```bash
python3 ./server.py 9005
ython3 ./client.py localhost 9005
```

To terminate the connection, simply type "Exit".