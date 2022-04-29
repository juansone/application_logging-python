#! python3

import pyautogui #Import pyautogui
import time #Import Time
import logging #Import logging module

while True: #Start loop
    logging.basicConfig(filename='mouse_movement-INFO.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p') #filemode='w' to re-write file every run (old logs lost)
    logging.info(pyautogui.position())
    print (pyautogui.position())
    time.sleep(1)
