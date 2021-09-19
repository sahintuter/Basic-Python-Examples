import pyautogui
import time

time.sleep(1)
count = 0
pyautogui.click(10, 5)
while True:
    pyautogui.FAILSAFE=True
    pyautogui.write(f" 1coderr")

    count +=1
    pyautogui.press("ENTER")



