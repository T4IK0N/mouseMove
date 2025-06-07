import pyautogui
import random
import time
import sys


print("program has started")

while True:
    start_time = time.time()
    while time.time() - start_time < 30:
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        pyautogui.moveRel(dx, dy, duration=0.1)
        time.sleep(0.2)