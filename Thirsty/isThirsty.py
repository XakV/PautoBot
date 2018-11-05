#!/usr/bin/python3

import serial
import time

ardSdata = serial.Serial('/dev/ttyACM0', 9600)
while True:
    if ardSdata.inWaiting():
        print(ardSdata.readline())
    time.sleep(5)
    print("Snoozing a bit more")
    time.sleep(5)

