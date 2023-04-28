import time
import logging


from image_to_text import img2str
from img.screenshot import take_screenshot_around_cursor


from fuzzywuzzy import process
import mouse
import mss


def load_trash_list():
    trash_list = []
    with open('Trash.txt', 'r', encoding='utf-8') as file:
        trash_list = file.readlines()

    return trash_list


def match_fish_catch(trash_list):
    x = 0
    while True:
        try:
            catch = img2str(take_screenshot_around_cursor())
        except mss.ScreenShotError as e:
            catch = None

        if catch:
            print(catch)
            if not x:

                time.sleep(0.5)
                x = 1
                continue
            x = 0
            rate = process.extractOne(catch, trash_list)
            if rate[1] > 10 and rate[1] < 85 and len(rate[0]) > 4:
                print(rate)
                mouse.press(button='left') 
                time.sleep(0.2)
                mouse.release(button='left')
                time.sleep(0.5)
                mouse.press(button='left')   
                time.sleep(0.2)
                mouse.release(button='left')
                time.sleep(2)
              
            else:
                time.sleep(2)


def main():
    logging.getLogger().setLevel(logging.ERROR)
    time.sleep(3)
    trash_list = load_trash_list()
    match_fish_catch(trash_list)


if __name__ == '__main__':
    main()
