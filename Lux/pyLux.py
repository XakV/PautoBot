#!/usr/bin/python3

import board
import busio
import adafruit_tsl2561
import time

i2c = busio.I2C(board.SCL, board.SDA)
tsl = adafruit_tsl2561.TSL2561(i2c)
tsl.enabled = True
tsl.gain = 0
tsl.integration_time = 1
while True:
    print("Broadband = {}".format(tsl.broadband))
    print("Infrared = {}".format(tsl.infrared))
    print("Lux = {}".format(tsl.lux))
    try:
        time.sleep(3)
    except:
        break
