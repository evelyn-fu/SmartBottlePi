import serial
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
import pickle
from gpiozero import Button
from time import sleep

button = Button(15)

model = LinearRegression()
model.fit()

email = "test@bhagat.io"
url = "https://smartbottleserver.heroku.app/data"
ser = serial.Serial('/dev/ttyACM0', 115200)
while 1:
    if(ser.in_waiting > 0 and ser.readline()[-1] == "\n"):
        line = ser.readline()
        #"roll:angle1;pitch:angle2"
       # data = re.split(': |; ', line)
        #roll = int(data[1])
        #pitch = int(data[3])
        if len(line.split(" ")) > 1:
            roll, pitch = line.split(" ")


            r = requests.post(url, params={"roll": roll, "pitch": pitch, "email":email})
            


while True:
    if button.is_pressed:
        print("Pressed")
    else:
        print("Released")
    sleep(1)
            
        
