
import pandas as pd
from firebase import firebase
import csv
import time
import datetime
import os


firebase = firebase.FirebaseApplication('https://bancotestelstm-default-rtdb.firebaseio.com/', None)

def update_firebase():
    header_list = ['Time', 'Humidity', 'Temperature', 'pH', 'pHpred']
    df = pd.read_csv(r'/home/saulo/FarmSystemIoTDL/backend/databaseedge/sensordatalist.csv', names=header_list)

    get_temp = df['Temperature'].tail(1)
    get_time = df['Time'].tail(1)
    get_humi = df['Humidity'].tail(1)
    get_pH = df['pH'].tail(1)
    get_pHpred = df['pHpred'].tail(1)

    data = {
        "Time": get_time,
        "Humidity": get_humi,
        "Temperature": get_temp,
        "pH": get_pH,
        "pHpred": get_pHpred
    }
    

   
    result = firebase.post('/sensordata', {'Time': get_time.to_json(), 'Humidity': get_humi.to_json(), 'Temperature': get_temp.to_json(), 'pH': get_pH.to_json(), 'pHpred': get_pHpred.to_json()})
    print(result)
    

while True:
    update_firebase()
    time.sleep(60)




  