import pyautogui
import time

#Beginning actions
pyautogui.moveTo(1200,60)
pyautogui.click()

#Get report
try:
    target_6 = pyautogui.locateCenterOnScreen("Capture_6.png",confidence=0.85)
    target_7 = pyautogui.locateCenterOnScreen("Capture_7.png",confidence=0.85)
    target_8 = pyautogui.locateCenterOnScreen("Capture_8.png",confidence=0.85)
    target_9 = pyautogui.locateCenterOnScreen("Capture_9.png",confidence=0.85)
    target_11 = pyautogui.locateCenterOnScreen("Capture_11.png",confidence=0.85)
    
    pyautogui.click(target_6, clicks = 3)     #Move the mouse to target_6 coordinates and click
    time.sleep(0.1)          #Sleep for 0.1 seconds
    
    #TEXT_1: '07/01/2023'
    pyautogui.press("delete")     #Press the delete key
    pyautogui.press("0")     #Press the 0 key
    pyautogui.press("7")     #Press the 7 key
    pyautogui.press("/")     #Press the / key
    pyautogui.press("0")     #Press the 0 key
    pyautogui.press("1")     #Press the 1 key
    pyautogui.press("/")     #Press the / key
    pyautogui.press("2")     #Press the 2 key
    pyautogui.press("0")     #Press the 0 key
    pyautogui.press("2")     #Press the 2 key
    pyautogui.press("3")     #Press the 3 key
    pyautogui.click(target_7)     #Move the mouse to target_7 coordinates and click
    time.sleep(0.1)          #Sleep for 0.1 seconds
    
    #TEXT_2: '54000'
    pyautogui.press("5")     #Press the 5 key
    pyautogui.press("4")     #Press the 4 key
    pyautogui.press("0")     #Press the 0 key
    pyautogui.press("0")     #Press the 0 key
    pyautogui.press("0")     #Press the 0 key
    pyautogui.click(target_8)     #Move the mouse to target_8 coordinates and click
    time.sleep(0.1)          #Sleep for 0.1 seconds
    
    #TEXT_3: '54013'
    pyautogui.press("delete")     #Press the delete key
    pyautogui.press("delete")     #Press the delete key
    pyautogui.press("delete")     #Press the delete key
    pyautogui.press("delete")     #Press the delete key
    pyautogui.press("delete")     #Press the delete key
    pyautogui.press("5")     #Press the 5 key
    pyautogui.press("4")     #Press the 4 key
    pyautogui.press("0")     #Press the 0 key
    pyautogui.press("1")     #Press the 1 key
    pyautogui.press("3")     #Press the 3 key

    pyautogui.click(target_9)     #Move the mouse to target_9 coordinates and click

    time.sleep(0.1)          #Sleep for 0.1 seconds
    target_10 = pyautogui.locateCenterOnScreen("Capture_10.png",confidence=0.85)
    pyautogui.click(target_10)     #Move the mouse to target_10 coordinates and click

    time.sleep(0.1)          #Sleep for 0.1 seconds
    pyautogui.click(target_11)     #Move the mouse to target_11 coordinates and click
    time.sleep(10)          #Sleep for 10 seconds

    target_12 = pyautogui.locateCenterOnScreen("Capture_12.png",confidence=0.85)

    while True:
        if target_12 == None:
            print("None")
        else:
            pyautogui.click(target_12)     #Move the mouse to target_12 coordinates and click
            time.sleep(60)          #Sleep for 60 seconds
            pyautogui.moveTo(1000,100)
            target_13 = pyautogui.locateCenterOnScreen("Capture_13.png",confidence=0.85)
            pyautogui.click(target_13)     #Move the mouse to target_13 coordinates and click
            exit()
except:
    print("ERROR")
