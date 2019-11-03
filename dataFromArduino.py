import serial
from lr import LinearRegression
import pickle
from gpiozero import Button
from time import sleep
import numpy as np

button = Button(15)
model = None
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
last_pressed = False
print("test")
xs = []
ys = []

email = "test@bhagat.io"
url = "https://smartbottleserver.heroku.app/data"
ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    
    
    if(ser.in_waiting > 0):
        line = str(ser.readline())
        print(line)
        print(button.is_pressed)
        roll, pitch = None, None
        if len(line.split(" ")) > 1:
            roll, pitch = line.split(" ")
            roll = float(roll)
            print(pitch[:-4])
            pitch = float(pitch[:-4])
        if button.is_pressed:
            if roll != None:
                print("adding xs:", len(xs))
                xs.append([1, roll, pitch])
        else:
            if last_pressed:
                for x in xs:
                    ys.append(2.75 / len(xs))
                print("training model")
                model.fit(xs, ys)
                print("done training")

                with open('model.pkl', 'wb') as f:
                    pickle.dump(model, f)

            else:
                if roll != None:
                    drank = model.predict(np.array([1, roll, pitch]))
                    r = requests.post(url, data={"drank": drank})

        last_pressed = button.is_pressed
