


import os
import sys
import subprocess
from dash import Dash

#app = Dash(__name__)
#server = app.server




def main():
    


    # script to execute files frontend\dashfuncionando.py
    #os.chdir('C:\\Users\\saulo\\FARMSYSTEMIOTDL\\frontend')
    #subprocess.Popen(["python", "dashboard.py"])
    
    # script to execute subpross files backend\databaseedge\data.py at the same time
    os.chdir('C:\\Users\\saulo\\FARMSYSTEMIOTDL\\backend\\databaseedge')
    subprocess.Popen(["python", "data.py"])
    # script to execute files backend\forecastdeeplearningLSTM\previsao.py
    os.chdir('C:\\Users\\saulo\\FARMSYSTEMIOTDL\\backend\\forecastdeeplearningLSTM')
    subprocess.Popen(["python", "previsao.py"])
   # script to execute files backend\databasecloud\datacloud.py
    os.chdir('C:\\Users\\saulo\\FARMSYSTEMIOTDL\\backend\\databasecloud')
    subprocess.Popen(["python", "datacloud.py"])
    

if __name__ == "__main__":
   main()
   #app.run_server()
   #app.run_server(debug=True, use_reloader=False) # Turn off reloader if inside Jupyter

   












