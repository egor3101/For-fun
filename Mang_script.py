# packages
import os
import subprocess
import cv2
import numpy as np
import pyautogui as pg
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


while True:

    try:
        #webbrowser.open_new('http://www.python.org')
        # take a screenshot to store locally
        screenshot = pg.screenshot('screenshot.png')

        # take a screenshot to locate objects on
        #screenshot = pg.screenshot()

        # adjust colors
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # locate a single object in a screenshot
        board = pg.locateOnScreen('Green_call.jpg')

        # draw rectangle around the object
        cv2.rectangle(
            screenshot,
            (board.left, board.top),
            (board.left + board.width, board.top + board.height),
            (0, 255, 255),
            2
        )


        #Действия если звонок поступил:

        #Вызываем браузер для вызова Automa
        subprocess.call('C:/Program Files/Google/Chrome/Application/chrome.exe')



        # display screenshot in a window
        #cv2.imshow('Screenshot', screenshot)

        # escape condition
        #cv2.waitKey(0)

        # clean up windows
        #cv2.destroyAllWindows()

    #Ничего не делаем, чтобы цикл не останавливался
    except:
        pass
