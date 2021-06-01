import subprocess
import pyttsx3
import time

tts = pyttsx3.init()

count= 0 

ip_addresss = "127.0.0.1"

while True: 
     pingip = subprocess.Popen(['ping' , ip_addresss] , stdout=subprocess.PIPE)
     time.sleep(60)
     if(pingip.poll() == 0 ):
         print("Device " + ip_addresss + ": connected")

     elif(pingip.poll() != 0):
         print("Device " + ip_addresss + ": disconnected")
