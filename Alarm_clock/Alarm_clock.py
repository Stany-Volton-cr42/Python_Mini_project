from playsound import playsound
import time


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"  # it just clear the terminal and return the output

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed+= 1

        time_left = seconds - time_elapsed
        minute_left = time_left // 60  # it gives the intiger divistion
        seconds_left = time_left % 60  # 125 % 60 = 5
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minute_left:02d}:{seconds_left:02d}")

    playsound('G:\\Python_project\\Python_Littel_project\\alarm.mp3')


minutes = int(input("Enter the minutes you want to Wait: "))
seconds = int(input("Enter the second you want to wait: "))
total_seconds = minutes * 60  + seconds 
alarm(total_seconds)
