import pynput
import random
from pynput.keyboard import Key, Controller
import time
def met():
    keyboard = Controller()

    for i in range(164):
        s=random.randint(3,5)
        keyboard.press(str(s))
        keyboard.release(str(s))
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

 
time.sleep(5)
met()
print('Done')