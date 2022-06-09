# from pynput.keyboard import Key, Controller
# from pynput.mouse import Button, Controller
# import pynput.mouse    as ms
# import pynput.keyboard as kb
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

keyboard = KeyboardController()
mouse = MouseController()

###---INITIAL SETUP CONFIGURATION---###
cmd1 = "pls beg"
cmd2 = "pls postmemes"
cmd3 = "pls dig"
cmd4 = "pls hunt"
cmd5 = "pls fish"
cmd6 = "pls search"

cmd_delay = 1
cumulative_delay = 45

# Command 2a is a LEGACY command and will not work with the latest
# Dank Memer update and has been replaced with interactions buttons.
# Set your mouse to be positioned over one of the buttons and put the
# values into the mouseCoords variables below.

cmd2a = "fresh"
cmd2a_cooldown = 1

mouseCoords_x = 550
mouseCoords_y = 880

focusCoords_x = 750
focusCoords_y = 950

###---DEFINING COMMAND FUNCTIONS---###

def pls_postmemes():
    keyboard.type(cmd2)
    keyboard.tap(Key.enter)
    time.sleep(2.0)
    mouse.position = (mouseCoords_x, mouseCoords_y)
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    time.sleep(0.1)
    mouse.position = (focusCoords_x, focusCoords_y)
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)

def pls_search():
    keyboard.type(cmd6)
    keyboard.tap(Key.enter)
    time.sleep(2.0)
    mouse.position = (mouseCoords_x, mouseCoords_y)
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    time.sleep(0.1)
    mouse.position = (focusCoords_x, focusCoords_y)
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)

def pls_beg():
    keyboard.type(cmd1)
    keyboard.tap(Key.enter)

def pls_dig():
    keyboard.type(cmd3)
    keyboard.tap(Key.enter)

def pls_hunt():
    keyboard.type(cmd4)
    keyboard.tap(Key.enter)

def pls_fish():
    keyboard.type(cmd5)
    keyboard.tap(Key.enter)
###---PRE_FLIGHT CODE---###

print("Dank Memer bot will initialize in 30 seconds...")
print("Please get your discord window ready!")
time.sleep(5.0)
print("Dank Memer Bot v3.2.1 is initialized...")
keyboard.type("Dank Memer Bot v3.2.1 is initialized...")
keyboard.tap(Key.enter)
time.sleep(0.5)

###---MAIN LOOP---###
while True:
    time.sleep(cmd_delay)
    pls_postmemes()
    time.sleep(cmd_delay)
    time.sleep(1)
    pls_search()
    time.sleep(cmd_delay)
    time.sleep(1)
    pls_beg()
    time.sleep(cmd_delay)
    pls_dig()
    time.sleep(cmd_delay)
    pls_hunt()
    time.sleep(cmd_delay)
    pls_fish()
    time.sleep(cmd_delay)
    time.sleep(cumulative_delay)
