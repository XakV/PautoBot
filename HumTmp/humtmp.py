#!/usr/bin/python3

import board
import adafruit_si7021
import busio
import time
from Adafruit_IO import Client

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

aio = Client('aikidouke', 'b8ed837510b04e498157546e960da6e5')
io_temp_feed = aio.feeds('alexandria-temp')
io_humid_feed = aio.feeds('alexandria-humidity')



while True:
    if sensor.temperature:
       aio.send_data(io_temp_feed.key, sensor.temperature)
       # print(sensor.temperature)
    if sensor.relative_humidity:
       aio.send_data(io_humid_feed.key, sensor.relative_humidity)
       # print(sensor.relative_humidity) uncomment for debug
    time.sleep(300)
