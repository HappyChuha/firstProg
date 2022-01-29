from pygame import mixer
mixer.init()
mixer.music.load("lol.mp3")
mixer.music.set_volume(0.05)
mixer.music.play()
while True:
    print("Enter p for pause, r for resume, t for checking time elapsed and e for exiting")
    inp = input("")
    if inp == 'p':
        mixer.music.pause()
    elif inp == 'r':
        mixer.music.unpause()
    elif inp == 'e':
        mixer.music.stop()
        mixer.music.unload()
        print("bue")
        break
    elif inp == "t":
            timer = mixer.music.get_pos()
            timer = timer/1000
            print(str(timer))
    else:
        print("Wrong input")