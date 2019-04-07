import random
import os
import shutil
import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

columns = shutil.get_terminal_size().columns

with open('All.txt') as f:
    lines = f.read().splitlines()
random.shuffle(lines)
for l in lines:
    os.system('clear')
    stdscr.addstr(l.center(columns))
    stdscr.refresh()
    stdscr.getkey()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
