# script to run frontend\dashboard.py in heroku render



import os

import sys

import subprocess



def main():

# script to execute files frontend\dashfuncionando.py

 os.chdir("C:\\Users\\saulo\\FARMSYSTEMIOTDL\\frontend")
 subprocess.Popen(["python", "dashboard.py"])
 

if __name__ == "__main__":
    main()

