from pygame import mixer
mixer.init()
mixer.music.load("lolz.mp3")
mixer.music.set_volume(0.05)
mixer.music.play()
while True:
    print("Enter p for pause, r for resume, t for checking time elapsed, s for setting position and e for exiting")
    inp = input("")
    if inp == 'p':
        mixer.music.pause()
    elif inp == 'r':
        mixer.music.unpause()
    elif inp == 'e':
        mixer.music.stop()
        mixer.music.unload()
        for i in range(10):
            print("bue")
        break
    elif inp == "t":
        timer = mixer.music.get_pos()
        print(timer/1000)
    elif inp == 's':
        setposinp = float(input("Enter time to set to: "))
        mixer.music.set_pos(setposinp)
    else:
        print("Wrong input")
