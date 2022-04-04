"""Requires  https://openhardwaremonitor.org/ to be downloaded and launched to run"""

import random
import socket
import time
from datetime import datetime

import psutil
import wmi

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))
w = wmi.WMI(namespace='root/OpenHardwareMonitor')


try:
    while True:
        temperature_info = ', '.join([f'{sensor.Name}: {sensor.Value}°C'
                                      for sensor in w.Sensor() if sensor.SensorType == u'Temperature'])
        time_now = datetime.now().strftime('%H:%M:%S')
        data = f'Current time: {time_now}, random value: {random.randint(1, 10000)}, ' \
               f'% CPU: {psutil.cpu_percent()}, {temperature_info}'
        sock.send(data.encode('utf-8'))
        response = sock.recv(1024)
        print(response.decode('utf-8'))
        time.sleep(60)
except KeyboardInterrupt:
    sock.close()
except ConnectionResetError:
    print('An existing connection was forcibly closed by the remote host')
    sock.close()
