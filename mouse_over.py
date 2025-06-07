import pyautogui
import random
import time
import sys


print("program has started")

while True:
    start_time = time.time()
    while time.time() - start_time < 30:
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        pyautogui.moveRel(dx, dy, duration=0.1)
        time.sleep(60)