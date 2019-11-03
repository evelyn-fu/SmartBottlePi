import serial
import re

ser = serial.Serial('/dev/ttyUSB0', 115200)
while 1:
    if(ser.in_waiting >0):
        line = ser.readline()
        #"roll:angle1;pitch:angle2"
        data = re.split(': |; ', line)
        roll = int(data[1])
        pitch = int(data[3])

