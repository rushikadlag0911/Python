import time
import winsound
from win10toast import ToastNotifier

def timer(message,minutes):
    # windows Notification Instantiator
    notificator = ToastNotifier()
    #Notification details
    notificator.show_toast("Good Morning",f"Alarm will go off in {minutes} minutes..",duration=50)

    time.sleep(minutes*60)  #Pause script
    winsound.Beep(frequency=2000,duration=1000) # Alarm Sound

    notificator.show_toast("wake up",duration=50)

if __name__ == "__main__":
    message = "Hello Wake up..!"
    minutes = 1        # minutes
    timer(message,minutes)    
    