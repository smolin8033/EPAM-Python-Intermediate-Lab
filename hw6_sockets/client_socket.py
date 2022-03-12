import random
import socket
import time
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.10', 9999))

while True:
    time_now = datetime.now().strftime('%H:%M:%S')
    data = f'Current time: {time_now}, value: {random.randint(1, 10000)}'
    sock.send(data.encode('utf-8'))
    response = sock.recv(1024)
    print(response.decode('utf-8'))
    time.sleep(60)

sock.close()
