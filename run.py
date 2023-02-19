


import os
import sys
import subprocess




def main():
    


    
    os.chdir("C:\\Users\\saulo\\FARMSYSTEMIOTDL\\frontend")
    subprocess.Popen(["python", "dashboard.py"])
    
    os.chdir("C:\\Users\\saulo\\FARMSYSTEMIOTDL\\backend\\databaseedge")
    subprocess.Popen(["python", "data.py"])
    
    os.chdir("C:\\Users\\saulo\\FARMSYSTEMIOTDL\\backend\\forecastdeeplearningLSTM")
    subprocess.Popen(["python", "previsao.py"])
   
    os.chdir("C:\\Users\\saulo\\FARMSYSTEMIOTDL\\backend\\databasecloud")
    subprocess.Popen(["python", "datacloud.py"])
    

if __name__ == "__main__":
    main()













