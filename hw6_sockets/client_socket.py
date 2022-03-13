import psutil
import random
import socket
import time
import wmi
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.10', 9999))
w = wmi.WMI(namespace='root/OpenHardwareMonitor')


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

sock.close()
