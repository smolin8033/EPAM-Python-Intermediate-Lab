import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('192.168.0.10', 9999))
sock.listen(5)

while True:
    client, addr = sock.accept()
    print('Connected: ', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        udata = data.decode('utf-8')
        client.send(udata.upper().encode('utf-8'))

    client.close()
    sys.exit()
