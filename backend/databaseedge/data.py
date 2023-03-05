

if __name__ == '__main__':

 
   
    
    import sqlite3
import serial
import datetime
import time
import pandas as pd
import csv
from datetime import datetime



PORT = 'COM4'
ser = serial.Serial('COM4', 115200, timeout=2)

humArray = []
tempArray = []
timeArray = []
pHArray = []
pHpredArray = []

while True:
    message = ser.readline()
    data = message.strip().decode('utf8')
    print(data)
    split_string = data.split(',')  # split string
    # converter a primeira parte da string em float
    humidity = float(split_string[0])
    # converter a segunda parte da string em float
    temperature = float(split_string[1])
    # converter a terceira parte da string em float
    pH = float(split_string[2])
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
   
    pHpred = pd.read_csv(r'C:\Users\saulo\FARMSYSTEMIOTDL\backend\databaseedge\predicaopH.csv', header=None)
    pHpred = pHpred.tail(1)
    pHpred = pHpred.values[0][0]
   

   
    print(dt_string, humidity, temperature,pH)
    humArray.append(humidity)  # adicionar valores de umidade ao array
    tempArray.append(temperature)  # adicionar valores de temperatura do array
    timeArray.append(dt_string)
    pHArray.append(pH)
    pHpredArray.append(pHpred)

    with open("sensordatalist.csv", "a") as f:
        writer = csv.writer(f, delimiter=",")
        
        writer.writerow([dt_string, humidity, temperature,pH,pHpred])

    df = pd.DataFrame(
        {'Time': timeArray, 'Humidity': humArray, 'Temperature': tempArray,'pH':pHArray,'pHpred':pHpredArray})
    print(df)

   
    header_list = ['Time', 'Humidity', 'Temperature','pH','pHpred']
    data = pd.read_csv('sensordatalist.csv', names=header_list)
    
    database = r"C:\Users\saulo\FARMSYSTEMIOTDL\backend\databaseedge\db\bancoedgeagro.db"
    conn = sqlite3.connect(database)
    '''conn = mysql.connect(host='localhost',
                  database='sensordatalist',
                     user='root',
                     password='sql_root_45t6')
     '''
    cursor = conn.cursor()

    
    cursor.execute('DROP TABLE IF EXISTS SensorValores;')

   
    criatabela = ''' CREATE TABLE SensorValores(
                   Time DATETIME, 
                   Humidity FLOAT, 
                   Temperature FLOAT,
                   pH FLOAT,
                     pHpred FLOAT 

    );'''

    cursor.execute(criatabela)
    
    for row in data.itertuples():  
        cursor.execute("""
                        INSERT INTO SensorValores(Time, Humidity, Temperature,pH,pHpred)
                        VALUES(?,?,?,?,?)
                        """,
                       (row.Time,
                        row.Humidity,
                        row.Temperature,
                        row.pH,
                        row.pHpred
                        ))

    print('Records are adding into table ..........')
    conn.commit()
