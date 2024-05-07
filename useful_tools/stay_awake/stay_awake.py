import random
import time
from datetime import datetime

from pyautogui import press


def derp():
    with open('word_file.txt', 'r') as word_file:
        n_words = random.randrange(10) + 1
        word_list = random.sample(word_file.read().splitlines(), n_words)

        for word in word_list:
            for letter in word:
                press(letter)
                time.sleep(random.randrange(50) / 100)
            press('space')
            time.sleep(random.randrange(100) / 100)
        time.sleep(random.randrange(50) / 100)
        press('enter')


def stay_awake():
    time.sleep(3)
    while True:
        if datetime.now().time() > datetime.strptime("1800", "%H%M").time():
            break
        try:
            derp()
            time.sleep(random.randrange(200) + 120)
        except:
            pass


if __name__ == '__main__':
    stay_awake()
