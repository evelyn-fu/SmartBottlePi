import serial
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
import pickle
from time import sleep


model = LinearRegression()
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)