from time import sleep
from tqdm import tqdm
import time
from sys import stdout

def ft_tqdm(lst: range):
    i = 1
    total = len(lst)
    bar_len = 60
    start = time.time()
    for val in lst:
        percent = int(i / total * 100)
        filled = int(bar_len * i // total)

        bar = ('=' * filled) + '>' + (' ' * (bar_len - filled - 1))

        elapsed = time.time() - start
        speed = i / elapsed if elapsed > 0 else 0

        stdout.write(f"\r{percent}%|[{bar}]| {i}/{total} ")
        stdout.flush()
        i+=1
        yield val

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()