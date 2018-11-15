#!/usr/bin/python3

import serial
import time
from Adafruit_IO import Client


# For https://io.adafruit.com/aikidouke/feeds/alexandria-soil-status
aio = Client('aikidouke', 'b8ed837510b04e498157546e960da6e5')
io_soil_status = aio.feeds('alexandria-soil-status')
ardSdata = serial.Serial('/dev/ttyACM0', 9600)
while True:
    if ardSdata.inWaiting():
        try:
            decoded_data = ardSdata.readline().decode("utf-8").split('"\"')[0]
            aio.send_data(io_soil_status.key, int(decoded_data))
        except:
            pass
        time.sleep(300)
#debug        print(int(ardSdata.readline()))
