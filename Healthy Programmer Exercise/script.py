from pygame import mixer
import os
from datetime import datetime
import time

os.system("CLS")
print("Welcome to the Healthy Programmer Application!\n")
print("This application starts at 9AM and lasts till 5PM\n")
print("During this time it reminds you the following:")
print("1) Drink water after every 45mins!")
print("2) Remove eyes from the screen after every 25mins!")
print("3) Do a physical activity after every 1hour!\n")

mixer.init()
while(1):
    time.sleep(1)
    now = datetime.now()
    current_time = int(now.strftime("%S"))

    if(current_time == 0):
        current_time = 60

    print("Current Time =", current_time)

    if(current_time % 25 == 0):
        mixer.music.load("Healthy Programmer Exercise\eye.mp3")
        mixer.music.set_volume(1.0)
        mixer.music.play()
    elif(current_time % 45 == 0):
        mixer.music.load("Healthy Programmer Exercise\water.mp3")
        mixer.music.set_volume(1.0)
        mixer.music.play()
    elif(current_time % 60 == 0):
        mixer.music.load("Healthy Programmer Exercise\physical.mp3")
        mixer.music.set_volume(1.0)
        mixer.music.play()
