import serial
import pandas as pd
from lr import LinearRegression
import pickle
from time import sleep


model = LinearRegression()
print(model.theta)
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    print(model.theta)