import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('192.168.0.10', 9999))
sock.listen(5)


def save_to_file(un_data):
    with open('text_file.txt', 'a') as file:
        file.write('{}\n'.format(un_data))


while True:
    client, addr = sock.accept()
    print('Connected: ', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        udata = data.decode('utf-8')
        save_to_file(udata)
        client.send(udata.upper().encode('utf-8'))

    client.close()
    sys.exit()
