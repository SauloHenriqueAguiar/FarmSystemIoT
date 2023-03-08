

import os
import json
import time
import math
import matplotlib.pyplot as plt
import serial
import numpy as np
import pandas as pd
from core.data_processor import DataLoader
from core.model import Model

fig = plt.figure(facecolor='white')

def plot_results(predicted_data, true_data):
    
    print ("Dados Reais:",true_data)
    print ("Previsão:",predicted_data)
    








def main():
    
    configs = json.load(open('config.json', 'r'))
    if not os.path.exists(configs['model']['save_dir']): os.makedirs(configs['model']['save_dir'])

    model = Model()
    model.build_model(configs)
    

    seq_len=configs['data']['sequence_length'],
    sensor_data= []
    predictions_data = []
    live_data = np.arange(seq_len[0]-1) 
    
    
    
    header_list = ['Time', 'Humidity', 'Temperature','pH','pHpred']

    df = pd.read_csv(r'C:\Users\saulo\FARMSYSTEMIOTDL\backend\databaseedge\sensordatalist.csv', names=header_list)

    get_temp = df['Temperature'].tail(20)
    get_time = df['Time'].tail(20)
    get_humi = df['Humidity'].tail(20)
    get_pH = df['pH'].tail(1)

    sensor_port = get_pH


    plt.ion() 

    while True:
        i=0
        while i < seq_len[0]-1:              # armazenar os dados de entrada no array de dados de teste
            #b = sensor_port.readline()         # ler uma string de bytes
            #live_data[i]= float(b.decode())
            live_data[i]= sensor_port
            sensor_data.append(live_data[i])
            i+=1    
        sensor_struct_data = live_data[np.newaxis,:,np.newaxis] #construir dados ao vivo para LSTM
        predictions= model.predict_sequence_live(sensor_struct_data, configs['data']['sequence_length']) #Mude a janela em 1 nova previsão a cada vez, execute novamente as previsões na nova janela
        predictions_data.append(predictions)

        plot_results(predictions_data[-120:],sensor_data[-100:])
        #plt.show()
        #plt.pause(1) #critical to display continous img  
        #time delay for 1 second for print plot_results
        time.sleep(1)
         
        
        predict = predictions[-1]

        with open(r'C:\Users\saulo\FARMSYSTEMIOTDL\backend\databaseedge\predicaopH.csv', 'a',
                  #name columns pH
                    newline='', 
                    # remove blank lines
                    
                  ) as f:
            
           

            f.write(str(predict) + '\n')
            

        f.close()
        


      

        

                       
       

        
        
       
          

        
        if len(sensor_data) >10 * seq_len[0]:
            np.savetxt('data\sensor.csv', sensor_data, delimiter = ',', header='sensor_value')

        #carregar dados para treinamento
            data = DataLoader(
            os.path.join('data', configs['data']['filename']),
            configs['data']['train_test_split'],
            configs['data']['columns']
            )

            x, y = data.get_train_data(
                seq_len=configs['data']['sequence_length'],
                normalise=configs['data']['normalise']
                )

                
        # treinamento em memória
            model.train(
                x,
                y,
                epochs = configs['training']['epochs'],
                batch_size = configs['training']['batch_size'],
                save_dir = configs['model']['save_dir']
            )
            sensor_data =sensor_data[-100:]


   


if __name__ == '__main__':
    main()

