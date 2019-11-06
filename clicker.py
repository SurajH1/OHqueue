import os
import pyautogui, sys
import datetime
import keyboard

print('Press Ctrl-C to quit.')

print("Hover mouse over 'get help' button and press A")
while not keyboard.is_pressed('a'):
    print(" ")
my_position = pyautogui.position()
try:
    pyautogui.moveTo(my_position)
    while 1:
        time = datetime.datetime.now()
        if datetime.datetime.now().minute == 1:
            if datetime.datetime.now().second > 1:
                break
        print(datetime.datetime.now())
        if keyboard.is_pressed('q'):
            break
    pyautogui.click()
    pyautogui.click()

except KeyboardInterrupt:
    print('\n')