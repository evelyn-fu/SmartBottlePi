import serial
from lr import LinearRegression
import pickle
from gpiozero import Button
from time import sleep
import numpy as np
import requests

button = Button(15)
model = None
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
last_pressed = False
print("test")
xs = []
ys = []

email = "test@bhagat.io"
url = "http://smartbottleserver.herokuapp.com/data"
ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    
    
    '''if(ser.in_waiting > 0):
        line = str(ser.readline())
        print(line)
        print("true")
        print(button.is_pressed)
        roll, pitch = None, None
        if len(line.split(" ")) > 1:
            roll, pitch = line.split(" ")
            print(pitch)
            if np.abs(float(pitch[:-4])) > 90:
                r = requests.post(url, data={"drank": 0.01})'''
    if button.is_pressed:
        print("sent")
        r = requests.post(url, data={"drank": 0.01})
