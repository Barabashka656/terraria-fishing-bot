import mss
import cv2
import numpy as np
import pyautogui


def take_screenshot_around_cursor() -> np.ndarray:
    
    current_position = pyautogui.position()
    mon = {"top": current_position.y - 90, "left": current_position.x - 190, "width": 350, "height": 80}
    sct = mss.mss()
    rgb_img = np.asarray(sct.grab(mon))
    
    gray_img = np.asarray(cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY))
    
    cv2.imwrite(r'img\area_of_visibility.png', gray_img)
    return gray_img
