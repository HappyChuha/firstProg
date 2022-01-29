from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load("alarm.mp3")
mixer.music.set_volume(0.1)
while True:
    sleep(1)
    mixer.music.play(999999999)
    if mixer.music.get_busy:
        print("Enter yes if drank water")
        inp = input()
        if inp == "yes":
            mixer.music.stop()
        else:
            print("Enter yes you probably capitalised the letters")
            continue