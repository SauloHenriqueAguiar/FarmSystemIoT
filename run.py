


import os
import sys
import subprocess
import time

def main():
    


    # script to execute files frontend\dashfuncionando.py
    os.chdir("./frontend")
    subprocess.Popen(["python", "dashboard.py"])
    
    # script to execute subpross files backend\databaseedge\data.py at the same time
    os.chdir("../backend/databaseedge")
    subprocess.Popen(["python", "data.py"])
    # script to execute files backend\forecastdeeplearningLSTM\previsao.py
    os.chdir("../forecastdeeplearningLSTM")
    subprocess.Popen(["python", "previsao.py"])
   # script to execute files backend\databasecloud\datacloud.py
    os.chdir("../databasecloud")
    subprocess.Popen(["python", "datacloud.py"])
    

if __name__ == "__main__":
   main()
   time.sleep(10)
   
   
   
   

   












