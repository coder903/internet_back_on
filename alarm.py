import urllib.request
import subprocess
from time import sleep

while 1:
    try:
        response = urllib.request.urlopen('https://expertcoders.net') #Try to connect to a website
        break #If it does not throw an error break out of loop
    except:
        #Couldn't connect. Error thrown
        print("Internet Not Connected")
        sleep(5)
        subprocess.call("clear")
        print("Checking Internet")
    sleep(10)    
while 1: #Internet must be on because we are here
    subprocess.call("bash noise.sh", shell=True) #Make noise
    print("Internet is now working")
    sleep(1)
    