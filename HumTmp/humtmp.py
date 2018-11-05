#!/usr/bin/python3

import board
import adafruit_si7021
import busio
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

while True:
    print("Temperature is {}".format(sensor.temperature))
    print("Humidity is {}".format(sensor.relative_humidity))
    time.sleep(1)

