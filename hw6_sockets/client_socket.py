import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.10', 9999))

while True:
    data = input()
    if data == 'q':
        break
    sock.send(data.encode('utf-8'))
    response = sock.recv(1024)
    print(response.decode('utf-8'))
sock.close()
