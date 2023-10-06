"""
Created by: Kyle Lyver
Created on: Oct 2023
This module shows all of the color possibilites of a RGB LED on a Micro:Bit
"""

from microbit import *

while True:
    if button_a.is_pressed():
        pin16.write_digital(1)
        display.scroll("Red")
    sleep(1)
    pin16.write_digital(0)
    pin15.write_digital(1)
    display.scroll("Green")
    sleep(1)
    pin15.write_digital(0)
    pin14.write_digital(1)
    display.scroll("Blue")
    sleep(1)
    pin14.write_digital(0)
    pin16.write_digital(1)
    pin14.write_digital(1)
    display.scroll("Magenta")
    sleep(1)
    pin16.write_digital(0)
    pin14.write_digital(0)
    pin16.write_digital(1)
    pin15.write_digital(1)
    display.scroll("Yellow")
    sleep(1)
    pin16.write_digital(0)
    pin15.write_digital(0)
    pin15.write_digital(1)
    pin14.write_digital(1)
    display.scroll("Cyan")
    sleep(1)
    pin15.write_digital(0)
    pin14.write_digital(0)
    pin16.write_digital(1)
    pin14.write_digital(1)
    pin15.write_digital(1)
    display.scroll("White")
    sleep(1)
    pin16.write_digital(0)
    pin15.write_digital(0)
    pin14.write_digital(0)
