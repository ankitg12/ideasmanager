import random
import os
import shutil

columns = shutil.get_terminal_size().columns

with open('All.txt') as f:
    lines = f.read().splitlines()
random.shuffle(lines)
for l in lines:
    os.system('clear')
    print(l.center(columns))
    input("")
