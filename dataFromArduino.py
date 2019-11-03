import serial
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
import pickle
from gpiozero import Button
from time import sleep

button = Button(15)
model = None
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

model = LinearRegression()

sleep(100)
last_pressed = False

xs = []
ys = []

email = "test@bhagat.io"
url = "https://smartbottleserver.heroku.app/data"
ser = serial.Serial('/dev/ttyACM0', 115200)
while 1:
    if(ser.in_waiting > 0 and ser.readline()[-1] == "\n"):
        if button.is_pressed:

            line = ser.readline()
            if len(line.split(" ")) > 1:
                roll, pitch = line.split(" ")
                xs.append([roll, pitch])
        else:
            if last_pressed:
                for x in xs:
                    ys.append(2.75 / len(xs))
                model.fit(xs, ys)

                with open('model.pkl', 'wb') as f:
                    pickle.dump(model, f)


        last_pressed = button.is_pressed
            # r = requests.post(url, params={"roll": roll, "pitch": pitch, "email":email})
