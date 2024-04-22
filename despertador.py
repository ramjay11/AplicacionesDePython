#
from playsound import playsound
import time

mp3_path = r"G:\Musixx@@\Fearless Iranians From Hell\Die For Allah\Fearless Iranians From Hell - Kneel to No One.mp3"

# playsound(mp3_path)

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarma(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}La alarma sonará: {minutes_left:02d}:{seconds_left:02d}") # Format number to 00:00

    playsound(mp3_path)    

minutes = int(input("Cuantos minutos esperar: "))
seconds = int(input("Cuantos segundos esperar: "))
total_seconds = minutes * 60 * seconds
alarma(10)