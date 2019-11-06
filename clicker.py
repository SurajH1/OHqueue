import os
import pyautogui, sys
import datetime
import keyboard
import time
from pynput.keyboard import Key, Controller

print('Press Ctrl-C to quit.')
hours, minutes = input("enter the time Office Hours opens up (Hours(24-hr format) Minutes)").split()
hours = int(hours)
minutes = int(minutes)

#print(type(hours))
print("Hover mouse over 'get help' button and press A")
my_keyboard = Controller()
while not keyboard.is_pressed('a'):
    pass
my_position = pyautogui.position()
try:
    pyautogui.moveTo(my_position)
    while 1:
        time = datetime.datetime.now()
        if datetime.datetime.now().minute == minutes:
            if datetime.datetime.now().second >= 0:
                break
        #print(datetime.datetime.now())
        if keyboard.is_pressed('q'):
            break
    pyautogui.moveTo(my_position)
    my_keyboard.press(Key.f5)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.click()

except KeyboardInterrupt:
    print('\n')