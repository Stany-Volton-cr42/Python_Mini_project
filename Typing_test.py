import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):

    stdscr.clear()
# stdscr same as print statement in curses module. it means standard screen
        # and 1 and 2 is co ordinate of the text for printing in terminal
    stdscr.addstr("Welcome to this Typing Test")
    stdscr.addstr("\nREMEMBER:- ",curses.color_pair(2))
    stdscr.addstr("Press CAPITAL (Q) key for Quit... \n",curses.color_pair(1))
    stdscr.addstr("Press ENTER to START... ",curses.color_pair(3))
    stdscr.refresh()
        # this is to hold the text in terminal untill the user type any key
    stdscr.getkey()


def Display_text(stdscr,target,current,wpm=0):
        stdscr.addstr(target)
        stdscr.addstr(1, 0, f"WPM {wpm}")

    # for overwrite the and changing the color according to right or wrong charetator
        for i,char in enumerate(current):
            current_char = target[i]
            color = curses.color_pair(1)
            if char != current_char:
                color = curses.color_pair(2)

            stdscr.addstr(0,i, char, color)


def load_text():
    try:
        with open ("G:\\Python_project\\Python_Littel_project\\text.txt","r") as f:
            lines = f.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError:
        print("File 'text.txt' not found.")
    except PermissionError:
        print("Permission denied to read 'text.txt'.")
    except Exception as e:
        print("Error:", e)
    return ""



def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:

        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        Display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        # this is exit the program and 113 is the ASCII value for (q)
        if ord(key) == 81:
            break
        
        # removing text using backspace
        if key in ('KEY_BACKSPACE','\b','\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    # THIS IS FOR TEXT COLOR IN TERMINAL USING CURSES LIBRARY
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press CAPITAL (Q) to Quit or any key to start.... ")
        key = stdscr.getkey()
        if ord(key) == 81:
            break

wrapper(main)