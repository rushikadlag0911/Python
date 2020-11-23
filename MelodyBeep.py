import winsound

def play_sound(frequency,duration):

    winsound.Beep(frequency,duration)

def melody():
    play_sound(1500,4555)
    play_sound(800,4400)

if __name__ == "__main__":
    melody()    