import sys
import time
import RPi.GPIO as GPIO

"""
Hour bits - Pin: 8, 10, 12, 16, 18
Minutes bits - Pin: 19, 21, 23, 22, 24, 26
Seconds bits - Pin: 3, 5, 7, 11, 13, 15
"""

pin_mapping = {"hour": [8, 10, 12, 16, 18],
               "minute": [19, 21, 23, 22, 24, 26],
               "second": [3, 5, 7, 11, 13, 15]}

def set_all_gpio_out():
    for k in pin_mapping:
        for pin in pin_mapping[k]:
            GPIO.setup(pin, GPIO.OUT)


def turn_off_all_pins():
    for k in pin_mapping:
        for pin in pin_mapping[k]:
            GPIO.output(pin, 0)


def sequential_test():
    for k in ['hour', 'minute', 'second']:
        for pin in pin_mapping[k]:
            GPIO.output(pin, 1)
            time.sleep(1)
            GPIO.output(pin, 0)


if '__main__' == __name__:
    
    GPIO.setmode(GPIO.BOARD)
    set_all_gpio_out()
    turn_off_all_pins()
    
    if len(sys.argv) > 1 and 'test' == sys.argv[1]:
        sequential_test()
