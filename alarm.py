import platform, urllib.request, subprocess
from win32com.client import Dispatch
from time import sleep

while 1:
    try:
        response = urllib.request.urlopen('https://expertcoders.net') # try to connect to a website
        if platform.system() == 'Windows':
            Dispatch("SAPI.Spvoice").Speak("Internet is on!")
        else:
            subprocess.call("bash noise.sh", shell=True)

    except:
        # not connected, so we're here
        if platform.system() == 'Windows':
            Dispatch("SAPI.Spvoice").Speak("Internet is off")
        else:
            subprocess.call("clear")
    sleep(10)
