
import pyautogui
import threading
import random
import sys
import signal


# handles the signal
def signal_handler(signal, frame):
    print('ctrl + c')
    sys.exit(0)


# listening to the ctrl c event or any other keyboard interruptions
signal.signal(signal.SIGINT, signal_handler)


""" setinterval is functio that takes a function and no of seconds
its recursive function creates a thread for every t seconds and call the function """


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def moveMouse():
    # taking width and height
    width = pyautogui.size().width
    height = pyautogui.size().height

    # generating random width and height
    randomWidth = random.randint(0, width)
    randomHeight = random.randint(0, height)

    # logging randomwidth and random height
    print(randomWidth, randomHeight)
    if(randomHeight <= 100):
        randomHeight = 196

    # moving mouse to the particular position
    pyautogui.moveTo(randomWidth, randomHeight, duration=1)
    pyautogui.click(randomWidth, randomHeight)
    pyautogui.write('hello world')


# setting interval to call function evry t seconds
t = set_interval(moveMouse, 10)
