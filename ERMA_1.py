import pyautogui
import time

#Beginning actions
pyautogui.moveTo(1700,200)
pyautogui.click()
time.sleep(1)          #Sleep for 1 second
target_main = pyautogui.locateCenterOnScreen("Capture_Main.png",confidence=0.85)
pyautogui.click(target_main)     #Move the mouse to target_main coordinates and click

#Relog to access Tracking Report
try:
    target_1 = pyautogui.locateCenterOnScreen("Capture_1.png",confidence=0.85)
    pyautogui.click(target_1)     #Move the mouse to target_1 coordinates and click

    time.sleep(1)          #Sleep for 1 second
    target_2 = pyautogui.locateCenterOnScreen("Capture_2.png",confidence=0.85)
    pyautogui.click(target_2)     #Move the mouse to target_2 coordinates and click

    time.sleep(1)          #Sleep for 1 second
    target_3 = pyautogui.locateCenterOnScreen("Capture_3.png",confidence=0.85)
    pyautogui.click(target_3)     #Move the mouse to target_3 coordinates and click

    time.sleep(8)          #Sleep for 8 second
    target_4 = pyautogui.locateCenterOnScreen("Capture_4.png",confidence=0.85)
    pyautogui.click(target_4)     #Move the mouse to target_4 coordinates and click

    time.sleep(5)          #Sleep for 5 seconds
    target_5 = pyautogui.locateCenterOnScreen("Capture_5.png",confidence=0.85)
    pyautogui.click(target_5)     #Move the mouse to target_5 coordinates and click       
except:
    print("ERROR")

#Launch second step to access Tracking Report
time.sleep(2)          #Sleep for 2 second
import ERMA_2.py
