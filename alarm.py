import urllib.request
import subprocess
from time import sleep

while 1:
    try:
        response = urllib.request.urlopen('https://geospect.com')
        break        
    except:
        print("Internet Not Connected")
        sleep(5)
        subprocess.call("clear")
        print("Checking Internet")
    sleep(10)    
while 1:
    subprocess.call("/home/mike/bin/beep.sh", shell=True)
    print("Internet is now working")
    sleep(1)
    