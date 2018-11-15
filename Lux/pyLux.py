#!/usr/bin/python3

import board
import busio
import adafruit_tsl2561
import time
from Adafruit_IO import Client

i2c = busio.I2C(board.SCL, board.SDA)
tsl = adafruit_tsl2561.TSL2561(i2c)
tsl.enabled = True
tsl.gain = 0
tsl.integration_time = 1

# For https://io.adafruit.com/aikidouke/feeds/alexandria-lux-readings
aio = Client('aikidouke', 'b8ed837510b04e498157546e960da6e5')
io_lux_feed = aio.feeds('alexandria-lux-readings')



while True:
    if tsl.lux:
        aio.send_data(io_lux_feed.key, tsl.lux)
    time.sleep(300)
