from time import sleep
from utils import prompt, match_failed
from PIL import ImageGrab
from ImageMatching import image_matching
import cv2 as cv
import numpy as np
import pyautogui

step_id = 0

print("============================================")
print('''
  _____        _          ____          _   
 |  __ \      | |        |  _ \        | |  
 | |__) |__ _ | | ______ | |_) |  ___  | |_ 
 |  ___// _` || ||______||  _ <  / _ \ | __|
 | |   | (_| || |        | |_) || (_) || |_ 
 |_|    \__,_||_|        |____/  \___/  \__|
                                              ver 1.0''')
print("============================================")
sleep(2)
choice = prompt()

if choice != 0:  # Making it match with the case statements in image_matching
    choice = choice + 9

# If 5 miss matches occurs, pal-bot is missing matching pattern
# image by a threshold, for this program, threshold is set at 0.80.
# Program will exit with assertive statement.
missedMatched = 0

while True:

    # Get screenshot from window capture
    img = cv.cvtColor(np.array(ImageGrab.grab((0, 0, 1980, 1800))), cv.COLOR_BGR2RGB)

    if step_id == 0:
        # User walks up to the bench and clicks 'f'
        # bot locates item and clicks it
        print("=== ACTION 1: Pal-bot is locating item and attempting to click it === ")
        res = image_matching(img, choice)
        if res is None:
            if missedMatched == 5:
                match_failed(step_id)
                break
            missedMatched = missedMatched + 1
            continue
        (top_left, bottom_right) = res
        centerX, centerY = int(((top_left[0] + bottom_right[0]) / 2)), int(((top_left[1] + bottom_right[1]) / 2))
        pyautogui.moveTo(centerX, centerY, 2, pyautogui.easeOutQuad)
        pyautogui.click()

        step_id = step_id + 1
        continue
    elif step_id == 1:
        # bot locates 'MAX' button and clicks it
        print("=== ACTION 2: Pal-bot is locating 'MAX' and attempting to click it === ")
        res = image_matching(img, step_id)
        if res is None:
            if missedMatched == 5:
                match_failed(step_id)
                break
            missedMatched = missedMatched + 1
            continue
        (top_left, bottom_right) = res
        centerX, centerY = int(((top_left[0] + bottom_right[0]) / 2)), int(((top_left[1] + bottom_right[1]) / 2))
        pyautogui.moveTo(centerX, centerY, 2, pyautogui.easeOutQuad)
        pyautogui.click()

        step_id = step_id + 1
        continue
    elif step_id == 2:
        # bot locates 'Start production' button and clicks it
        print("=== ACTION 3: Pal-bot is locating 'Start production' and attempting to click it === ")
        res = image_matching(img, step_id)
        if res is None:
            if missedMatched == 5:
                match_failed(step_id)
                break
            missedMatched = missedMatched + 1
            continue
        (top_left, bottom_right) = res
        centerX, centerY = int(((top_left[0] + bottom_right[0]) / 2)), int(((top_left[1] + bottom_right[1]) / 2))
        pyautogui.moveTo(centerX, centerY, 2, pyautogui.easeOutQuad)
        pyautogui.click()

        step_id = step_id + 1
        continue
    elif step_id == 3:
        # bot holds the F key
        print("=== ACTION 4: Pal-bot is holding down 'F' key === ")
        pyautogui.keyDown('f')
        step_id = step_id + 1
        continue
    elif step_id == 4:
        #   Continue to hold F until 'Acquire' text box appears
        #   While holding F, if 'Acquire' text box appears unhold 'F' key
        #   click the 'F' key again to get the items
        #   Exit with closing routine
        print("=== ACTION 4: Pal-bot is holding down 'F' key === ")
        res = image_matching(img, step_id)
        if res is None:
            continue
        print("=== ACTION 5: Pal-bot is acquiring item(s) === ")
        pyautogui.keyUp('f')
        sleep(1)

        pyautogui.keyDown('f')
        sleep(1)

        pyautogui.press('f')
        print("!!! Finished !!!")
        break


print('Exiting...')